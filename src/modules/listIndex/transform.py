import os
import pandas as pd

def keep_index(data: dict):
  try:
    df = pd.DataFrame(data['results'])
    return df['index']
  except Exception as e:
    print(f"An error has occurred ==> {e}")
    raise