import os
import json

def transform_data (dataList: list):
  try:
    data = json.dumps(dataList)
    return data
  except Exception as e:
    print(f"An error has occurred ==> {e}")
    raise