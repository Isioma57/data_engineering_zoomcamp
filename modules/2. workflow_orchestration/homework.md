## Module 2 Homework

The goal will be to construct an ETL pipeline that loads the data, performs some transformations, and writes the data to a database (and Google Cloud!).

- Create a new pipeline, call it `green_taxi_etl`
- Add a data loader block and use Pandas to read data for the final quarter of 2020 (months `10`, `11`, `12`).
  - You can use the same datatypes and date parsing methods shown in the course.
  - `BONUS`: load the final three months using a for loop and `pd.concat`
- Add a transformer block and perform the following:
  - Remove rows where the passenger count is equal to 0 _and_ the trip distance is equal to zero.
  - Create a new column `lpep_pickup_date` by converting `lpep_pickup_datetime` to a date.
  - Rename columns in Camel Case to Snake Case, e.g. `VendorID` to `vendor_id`.
  - Add three assertions:
    - `vendor_id` is one of the existing values in the column (currently)
    - `passenger_count` is greater than 0
    - `trip_distance` is greater than 0
- Using a Postgres data exporter (SQL or Python), write the dataset to a table called `green_taxi` in a schema `mage`. Replace the table if it already exists.
- Write your data as Parquet files to a bucket in GCP, partioned by `lpep_pickup_date`. Use the `pyarrow` library!
- Schedule your pipeline to run daily at 5AM UTC.

### Questions

## Question 1. Data Loading

Once the dataset is loaded, what's the shape of the data?

* 266,855 rows x 20 columns ✅
* 544,898 rows x 18 columns
* 544,898 rows x 20 columns
* 133,744 rows x 20 columns

```py
import io
import pandas as pd
import requests
from pandas import DataFrame


if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):

    urls = ('https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-10.csv.gz',
            'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-11.csv.gz',
            'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-12.csv.gz'
    )


    greentrip_2020_final_quarter = pd.DataFrame()

    taxi_dtypes= {
        'VendorID': pd.Int64Dtype(),
        'passenger_count' : pd.Int64Dtype(),
        'trip_distance' : float,
        'RatecodeID' : pd.Int64Dtype(),
        'store_and_fwd_flag' : str,
        'PULocationID' : pd.Int64Dtype(),
        'DOLocationID' : pd.Int64Dtype(),
        'payment_type' : pd.Int64Dtype(),
        'fare_amount' : float,
        'extra'      :float,
        'mta_tax':float ,              
        'tip_amount':float  ,            
        'tolls_amount' :float ,       
        'improvement_surcharge':float ,   
        'total_amount' :float ,        
        'congestion_surcharge' :float
    }

    parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']

    for data in urls:
        green_data = pd.read_csv(data, compression="gzip",dtype=taxi_dtypes, sep=",", parse_dates = parse_dates)

        greentrip_2020_final_quarter = pd.concat([greentrip_2020_final_quarter,green_data])
    
    return greentrip_2020_final_quarter


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
```

## Question 2. Data Transformation

Upon filtering the dataset where the passenger count is greater than 0 _and_ the trip distance is greater than zero, how many rows are left?

* 544,897 rows
* 266,855 rows
* 139,370 rows ✅
* 266,856 rows

```py
import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    green_data = data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]

    green_data['lpep_pickup_datetime'] = pd.to_datetime(green_data['lpep_pickup_datetime'])
    green_data['lpep_dropoff_datetime'] = pd.to_datetime(green_data['lpep_dropoff_datetime'])
    
    green_data.columns=(data.columns
                    .str.replace('ID', '_id')
                    .str.lower()
    )

    return green_data


@test
def test_output(green_data, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert green_data is not None, 'The output is undefined'
    assert green_data['vendor_id'].isin([1, 2]).all(), "vendor_id contains invalid values"
    assert (green_data['passenger_count'] > 0).all(), "There are rows with passenger_count <= 0"
    assert (green_data['trip_distance'] > 0).all(), "There are rows with trip_distance <= 0"
```

## Question 3. Data Transformation

Which of the following creates a new column `lpep_pickup_date` by converting `lpep_pickup_datetime` to a date?

* `data = data['lpep_pickup_datetime'].date`
* `data('lpep_pickup_date') = data['lpep_pickup_datetime'].date`
* `data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date` ✅
* `data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt().date()`

## Question 4. Data Transformation

What are the existing values of `VendorID` in the dataset?

* 1, 2, or 3
* 1 or 2 ✅
* 1, 2, 3, 4
* 1

## Question 5. Data Transformation

How many columns need to be renamed to snake case?

* 3
* 6
* 2
* 4 ✅

Columns: `VendorID`, `RatecodeID`, `PULocationID` and `DOLocationID`

## Question 6. Data Exporting

Once exported, how many partitions (folders) are present in Google Cloud?

* 96 ✅
* 56
* 67
* 108

### Google Cloud Storage(Partioned)

```py
import pyarrow as pa
import pyarrow.parquet as pq
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ['GOOGLE_APPLICATION_CREDENTIALS']= '/home/src/key.json'

@data_exporter
def export_data(data, *args, **kwargs):

    bucket_name = 'my_bucket'
    project_id = 'my_project_id'

    table_name= 'green_taxi_final_quarter'

    root_path = f'{bucket_name}/{table_name}'

    data['lpep_pickup_date']=data['lpep_pickup_datetime'].dt.date

    table = pa.Table.from_pandas(data)

    gcs= pa.fs.GcsFileSystem()

    pq.write_to_dataset(
        table,
        root_path = root_path,
        partition_cols=['lpep_pickup_date'],
        filesystem=gcs
    )
```

