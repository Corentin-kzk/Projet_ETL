from ..core.data_frame import DataFrame
import pandas as pd

def apply_filters(data, directives) -> pd.DataFrame:
    df_to_filter = data.get()

    for fltr in directives:
        if not isinstance(fltr[0], list):
            df_to_filter = filter_dataframe(df_to_filter, fltr[0], fltr[1], fltr[2])
        else:
            df_list = []
            for sub_fltr in fltr:
                df_list.append(filter_dataframe(df_to_filter, sub_fltr[0], sub_fltr[1], sub_fltr[2]))
            df_to_filter = pd.concat(df_list)

    data.set(df_to_filter) 



def filter_dataframe(df_to_filter, column_name, condition, value_to_compare) -> DataFrame:

    if not isinstance(df_to_filter, pd.DataFrame):
        raise ValueError("Aucune Dataframe n'a été instanciée.")
    
    if isinstance(value_to_compare, list):
        value_length = len(value_to_compare)
    else:
        value_length = value_to_compare
    
    if condition == 'equal':
        df_to_filter = df_to_filter[df_to_filter[column_name].apply(lambda x: len(x) if isinstance(x, list) else x) == value_length]
    elif condition == 'bigger':
        df_to_filter = df_to_filter[df_to_filter[column_name].apply(lambda x: len(x) if isinstance(x, list) else x) > value_length]
    elif condition == 'lower':
        df_to_filter = df_to_filter[df_to_filter[column_name].apply(lambda x: len(x) if isinstance(x, list) else x) < value_length]
    elif condition == 'equal_or_bigger':
        df_to_filter = df_to_filter[df_to_filter[column_name].apply(lambda x: len(x) if isinstance(x, list) else x) >= value_length]
    elif condition == 'equal_or_lower':
        df_to_filter = df_to_filter[df_to_filter[column_name].apply(lambda x: len(x) if isinstance(x, list) else x) <= value_length]
    else:
        raise ValueError("La condition doit être 'equal', 'bigger', 'lower', 'equal_or_bigger', ou 'equal_or_lower'.")
    

    return df_to_filter
        
