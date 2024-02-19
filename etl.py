import sys

help = [
    {
        'value': '--export',
        'message': 'Data format to export'
    },
    {
        'value': '--help',
        'message': 'help message'
    }
]


# Define a function
def init():
    args = sys.argv[1:]
    if '--help' in args :
        if len(args) == 1 :
            res = next((sub for sub in help if sub['value'] == '--help'), None)
            print('this is help', res['message'])
        else:
            for arg in args:
                if arg != '--help':
                    res = next((sub for sub in help if sub['value'] == arg), None)
                    if res :
                        print(res['message'])
                    else :
                        print('this argument ' +  arg  +' is not valid')
    else:
        raise ('add value')


# Call function within module
try:
    init()
except:
    print('err')
