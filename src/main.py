import argparse
from termcolor import colored
import argcomplete
from services.core.yaml_interpretor import YamlInterpretor
from services.extract.extractor_handler import extract_handler
from services.transform.transform_handler import transform_handler
from services.load.load_handler import load_handler

ETL = dict()


def main():
    parser = argparse.ArgumentParser(description="ETL en ligne de commande en Python")
    parser.add_argument('-y', '--yaml_config', help='Path of the input yaml file', required=True)
    parser.add_argument('-etl', '--etl_config', help='choose your etl module', required=False, default='index_list')
    argcomplete.autocomplete(parser)
    args = vars(parser.parse_args())
    yaml_interpreter = YamlInterpretor(args['yaml_config'])
    try:
        orders = yaml_interpreter.open()
        extract, transform, load = yaml_interpreter.get_etl_orders(orders)
        extract_name = yaml_interpreter.get_name(extract)

        for name in extract_name:
            print(colored(f"EXTRACT: {name} !!!", 'green'))
            ETL[name] = extract_handler(extract[name])
            print(colored(f"TRANSFORM: {name} !!!", 'green'))
            transform_handler(transform[name], ETL[name])
            print(colored(f"LOAD: {name} !!!", 'green'))
            load_handler(load[name], ETL[name])


    except Exception as error:
        print(colored(f"ERROR: {error}", 'red'))


# Call function within module
if __name__ == "__main__":
    main()
