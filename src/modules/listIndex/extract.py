import os
import requests
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("BASE_DND_URL")
API_URL = BASE_URL + os.getenv("URL_DND_MONSTER_INDEX")

headers = {
  'Accept': 'application/json'
}

def get_api(headers=headers):
  try:
    response = requests.get(API_URL, headers)
    data = response.json()
    return data
  except Exception as e:
    print(f"An error has occurred ==> {e}")
    raise