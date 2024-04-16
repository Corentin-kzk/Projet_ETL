import yaml

class YamlInterpretor:
    def __init__(self, path):
        self.path = path

    def open(self):
        try :
            with open(self.path, 'r') as file:
                taskTodo = yaml.safe_load(file)
                return taskTodo
        except FileNotFoundError:
            raise FileNotFoundError("File not found")

    def get_etl_orders(self, yaml_opened):
        try:
            extractList, transformList, loadList = yaml_opened['EXTRACT'], yaml_opened['TRANSFORM'], yaml_opened[
                'LOAD']
            return extractList, transformList, loadList
        except Exception:
            raise ValueError("The main argument must be one of the following values: 'EXTRACT', 'TRANSFORM', 'LOAD'")

    def get_name(self, order):
        return list(order.keys())