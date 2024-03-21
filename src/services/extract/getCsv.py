import pandas as pd


def get_csv(path):
    try:
        data = pd.read_csv(path)
        json_data = data.to_json(orient='records', indent=4)
        return json_data
    except FileNotFoundError:
        raise FileNotFoundError
