from ..core.data_frame import DataFrame
import pandas as pd

def apply_type_filters(data, directives) -> pd.DataFrame:
    df_to_filter = data.get()

    for fltr in directives:
        if not isinstance(fltr[0], list):
            df_to_filter = filter_dataframe_by_type(df_to_filter, fltr[0], fltr[1])
        else:
            df_list = []
            for sub_fltr in fltr:
                df_list.append(filter_dataframe_by_type(df_to_filter, sub_fltr[0], sub_fltr[1]))
            df_to_filter = pd.concat(df_list)

    data.set(df_to_filter) 



def filter_dataframe_by_type(df_to_filter, column_name, value_type) -> DataFrame:
    if not isinstance(df_to_filter, pd.DataFrame):
        raise ValueError("Aucune Dataframe n'a été instanciée.")
    
    filtered_df = df_to_filter[df_to_filter[column_name].apply(lambda x: type(x).__name__) == value_type]

    return filtered_df
        
