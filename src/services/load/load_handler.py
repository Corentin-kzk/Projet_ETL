from .loadJson import load_json
from .loadCSV import load_csv

def order_handler(order_name, directive, df):
    match order_name:
        case 'json':
            return load_json(directive, df)
        case 'csv':
            return  load_csv(directive, df)
    raise ValueError(f'Unknown LOAD type: {order_name}')


def load_handler(orders, data):
    for order_id, order_data in orders.items():
        print(order_id, order_data)
        order_handler(order_id, order_data, data)
