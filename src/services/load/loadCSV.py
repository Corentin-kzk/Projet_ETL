from ..core.data_frame import DataFrame

def load_csv(fileName,df: DataFrame):
    try:
        df.to_csv(f"./{fileName}.csv")
        print(f"DataFrame contents exported to './{fileName}' successfully.")
    except Exception as e:
        print(f"An error occurred while exporting DataFrame to csv: {e}")