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
