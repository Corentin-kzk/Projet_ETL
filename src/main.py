import argparse
from termcolor import colored
import argcomplete
from services.core.yaml_interpretor import YamlInterpretor

def main():
    parser = argparse.ArgumentParser(description="ETL en ligne de commande en Python")
    parser.add_argument('-y', '--yaml_config', help='Path of the input yaml file', required=True)
    parser.add_argument('-etl', '--etl_config', help='choose your etl module', required=False, default='index_list')
    argcomplete.autocomplete(parser)
    args = vars(parser.parse_args())
    yaml_interpretor = YamlInterpretor(args['yaml_config'])
    try:
        orders = yaml_interpretor.open()
        extract, transform, load = yaml_interpretor.get_etl_orders(orders)
        extract_name = yaml_interpretor.get_name(extract)

        print(extract_name)
        print(f"extract : {extract}, transform : {transform}, load : {load}")

    except Exception as error:
        print(colored(f"ERROR: {error}", 'red'))


# Call function within module
if __name__ == "__main__":
    main()
