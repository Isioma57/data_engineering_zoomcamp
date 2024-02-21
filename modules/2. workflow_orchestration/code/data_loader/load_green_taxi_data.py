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

    green_tripdata_2020_quarter = pd.DataFrame()

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

        green_tripdata_2020_quarter = pd.concat([green_tripdata_2020_quarter,green_data])
    
    return green_tripdata_2020_quarter


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'