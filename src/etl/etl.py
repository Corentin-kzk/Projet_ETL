import argparse
def main():
    parser = argparse.ArgumentParser(description="ETL en ligne de commande en Python")
    parser.add_argument('--input_file',help='Chemin du fichier d\'entrée', required=False)
    parser.add_argument('--output_file', help='Chemin du fichier de sortie', required=True)

    args = parser.parse_args()
    print(args)


# Call function within module
if __name__ == "__main__":
    main()