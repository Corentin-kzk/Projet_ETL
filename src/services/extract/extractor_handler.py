from .getApi import getApi
from ..core.data_frame import DataFrame
import pandas as pd


def order_handler(order_name, directive):
    match order_name:
        case 'api':
            return getApi(directive)


def extract_handler(orders):
    df = None
    for order_id, order_data in orders.items():
        result = order_handler(order_id, order_data)
        if df is not None:
            df = pd.concat(df, DataFrame(result))
        else:
            df = DataFrame(result)
    if df is None:
        raise Exception('No data found')
    return df
