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
    raise ValueError(f'Unknown open type: {order_name}')


def extract_handler(orders):
    df = list()
    for order_id, order_data in orders.items():
        result = order_handler(order_id, order_data)
        df.append(DataFrame(result))
    if len(df) == 0:
        raise Exception('No data found')
    return df
