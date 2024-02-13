import os
import argparse
import requests
from time import time
import pandas as pd
from sqlalchemy import create_engine

# Function to download a file
def download_file(url):
    file_name = url.split('/')[-1]
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_name, 'wb') as file:
            file.write(response.content)
        return file_name
    else:
        print(f"Error: Unable to download the file. HTTP Status Code: {response.status_code}")
        return None

# Main function to process files and load into database
def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_trips = params.table_trips
    table_zones = params.table_zones
    urls = params.urls.split(',')

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    for url in urls:
        file_name = download_file(url)

        if file_name.endswith('.parquet'):
            df = pd.read_parquet(file_name, engine='pyarrow')
            converted_csv_name = file_name.replace('.parquet', '.csv')
            df.to_csv(converted_csv_name, index=False)
            df_iter = pd.read_csv(converted_csv_name, iterator=True, chunksize=500000)
            table_name = table_trips
        elif file_name.endswith('.csv'):
            df_iter = pd.read_csv(file_name, iterator=True, chunksize=100)
            table_name = table_zones
        else:
            raise ValueError("Unsupported file format")

        df = next(df_iter)
        df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace', index= False)
        df.to_sql(name=table_name, con=engine, if_exists='append', index=False)

        while True:
            try:
                t_start = time()
                df = next(df_iter)
                df.to_sql(name=table_name, con=engine, if_exists='append', index= False)
                t_end = time()
                print(f'Inserted another chunk, took {t_end - t_start:.3f} seconds')
            except StopIteration:
                print(f"Finished ingesting data from {file_name} into the PostgreSQL database")
                break

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest Data into Postgres')
    parser.add_argument('--user', required=True, help='username for postgres')
    parser.add_argument('--password', required=True, help='password for postgres')
    parser.add_argument('--host', required=True, help='host for postgres')
    parser.add_argument('--port', required=True, help='port for postgres')
    parser.add_argument('--db', required=True, help='database name for postgres')
    parser.add_argument('--table_trips', required=True, help='table name for Trips data')
    parser.add_argument('--table_zones', required=True, help='table name for Zones data')
    parser.add_argument('--urls', required=True, help='URLs for the CSV and Parquet files')

    args = parser.parse_args()
    main(args)
