import os
import json
from extract import get_monsters
from transform import transform_data

def load_json(data: json):
  folder_path = 'src/data'
  file_name = 'monsters.json'
  json_file_path = os.path.join(folder_path, file_name)

  if not os.path.exists(folder_path):
    os.makedirs(folder_path)

  with open(json_file_path, "w") as f:
    f.write(data)

  print(f"The '{json_file_path}' file has been successfully created.")

load_json(transform_data(get_monsters()))