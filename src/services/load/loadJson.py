from ..core.data_frame import DataFrame


def load_json(fileName,df: DataFrame):
    print(df.display())
    try:
        df.to_json(f"./{fileName}.json")
        print(f"DataFrame contents exported to './{fileName}' successfully.")
    except Exception as e:
        print(f"An error occurred while exporting DataFrame to JSON: {e}")

