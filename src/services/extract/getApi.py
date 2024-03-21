import requests

headers = {
    'Accept': 'application/json'
}


def get_api(path: str):
    try:
        response = requests.get(path, headers)
        data = response.json()
        return data
    except Exception:
        raise Exception
