from ..core.data_frame import DataFrame
def extract_by_tags(dataframe: DataFrame, keys):
    return dataframe.extract(keys)
