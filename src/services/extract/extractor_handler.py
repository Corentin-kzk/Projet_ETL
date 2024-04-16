from .getApi import get_api
from .getCsv import get_csv
from .getJson import get_json
from ..core.data_frame import DataFrame


def order_handler(order_name, directive):
    match order_name:
        case 'api':
            return get_api(directive)
        case 'csv':
            return get_csv(directive)
        case 'json':
            return get_json(directive)
    raise ValueError(f'Unknown EXTRACT type: {order_name}')


def extract_handler(orders):
    df = None
    for order_id, order_data in orders.items():
        result = order_handler(order_id, order_data)
        df = DataFrame(result)
    if df is None:
        raise Exception('No data found')
    return df
