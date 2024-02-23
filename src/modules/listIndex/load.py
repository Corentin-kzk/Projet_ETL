import os
import pandas as pd

def loadCsv(data: pd.core.frame.DataFrame):
  folder_path = 'src/data'
  file_name = 'listIndex.csv'
  csv_file_path = os.path.join(folder_path, file_name)

  if not os.path.exists(folder_path):
    os.makedirs(folder_path)


  if not os.path.exists(csv_file_path):
    data.to_csv(csv_file_path, index=False)
    print(f"The '{csv_file_path}' file has been successfully created.")
    return

  old_csv = pd.read_csv(csv_file_path)

  if old_csv.equals(data):
    print("No changes")
  else:
    data.to_csv(csv_file_path, index=False)
    print(f"The '{csv_file_path}' file has been successfully updated.")