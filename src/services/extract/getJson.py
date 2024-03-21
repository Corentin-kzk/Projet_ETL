import pandas as pd


def get_json(path):
    try:
        data = pd.read_json(path)
        return data
    except FileNotFoundError as e:
        raise FileNotFoundError(f"The specified file '{path}' does not exist.") from e
    except ValueError as e:
        raise ValueError(f"The JSON file '{path}' is malformed or not in the expected format.") from e
