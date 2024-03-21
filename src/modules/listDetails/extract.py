import os
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("BASE_DND_URL")
API_URL = BASE_URL + os.getenv("URL_DND_MONSTER_DETAILS")

folder_path = "src/data"
file_name = "listIndex.csv"
csv_file_path = os.path.join(folder_path, file_name)
json_name = "monsters.json"
json_file_path = os.path.join(folder_path, json_name)
headers = {
  'Accept': 'application/json'
}

def getMonsters(headers=headers):

  if not os.path.exists(folder_path) or not os.path.exists(csv_file_path):
    print("You need to extract index before.")
    raise ValueError("Missing folder or CSV file.")

  data = []
  df = pd.read_csv(csv_file_path)

  print("Please note that this will take some time.")

  for index, row in df.iterrows():
    monster_url = API_URL + row["index"]
    response = requests.get(monster_url, headers)
    if response.status_code == 200:
      data.append(response.json())
    else:
      print(f"Error fetching data for {row['index']}")

  return data