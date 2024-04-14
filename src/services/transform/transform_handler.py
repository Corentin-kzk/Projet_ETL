from .filter_by_order import filter_by_order
from .extract_by_tags import extract_by_tags


def order_handler(order_name, directive, data):
    match order_name:
        case 'filter':
            return extract_by_tags(data, directive.get('keys', []))
        case 'order':
            return filter_by_order(data, directive)
    raise ValueError(f'Unknown TRANSFORM type: {order_name}')


def transform_handler(orders, data):
    for order in orders:
        for order_id, order_data in order.items():
            order_handler(order_id, order_data, data)
