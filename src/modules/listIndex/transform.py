import os
import pandas as pd

def keepIndex(data: dict):
  try:
    df = pd.DataFrame(data['results'])
    return df['index']
  except Exception as e:
    print(f"An error has occurred ==> {e}")
    raise