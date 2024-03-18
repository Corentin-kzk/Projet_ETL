def order_handler(order_name, directive):
    match order_name:
        case 'filter':
            print(directive)
            return 'OK'
    raise Exception('Invalid filter name')

def transform_handler(orders, data) :
    for order_id, order_data in orders.items():
        print(order_id, order_data)
        order_handler(order_id, order_data)