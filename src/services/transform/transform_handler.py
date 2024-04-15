from .filter_by_order import filter_by_order
from .extract_by_tags import extract_by_tags
from .apply_filters import apply_filters
from .get_needed_keys import get_needed_keys
from ..core.data_frame import DataFrame

def order_handler(order_name, directive, data: DataFrame):
    match order_name:
        case 'filter':
            return extract_by_tags(data, directive.get('keys', []))
        case 'order':
            return filter_by_order(data, directive)
        case 'keys_needed':
            return get_needed_keys(data, directive)
        case 'filter_by':
            return apply_filters(data, directive)
    raise ValueError(f'Unknown TRANSFORM type: {order_name}')


def transform_handler(orders, data):
    for order in orders:
        for order_id, order_data in order.items():
            order_handler(order_id, order_data, data)


