from pandas import DataFrame, json_normalize, concat

class Transform:
    df: DataFrame = None
    def __init__(self, monsterList=[]):
        self.monsterList = monsterList

    def _recursive_search(self, nested_dict, keys):
        if len(keys) == 1:
            if isinstance(nested_dict, list):
                return [item.get(keys[0]) for item in nested_dict if item and keys[0] in item]
            else:
                return nested_dict.get(keys[0])

        if keys[0] not in nested_dict:
            return None 

        if isinstance(nested_dict.get(keys[0]), list):
            result = []
            value = None
            for item in nested_dict.get(keys[0]):
                value = self._recursive_search(item, keys[1:])
                result.append(value)
    
            return result if len(result) > 1 else value

        return self._recursive_search(nested_dict.get(keys[0]), keys[1:])

    def filter_json(self, keys_needed) -> dict:
        filtered_monsters = []

        for monster in self.monsterList:
            filtered_monster = {}
            for key in keys_needed:
                nested_keys = key.split('.')
                if key not in filtered_monster:
                    filtered_monster[key] = {}
                if len(nested_keys) > 1:
                    if nested_keys[1] not in filtered_monster[key]:
                        filtered_monster[key] = self._recursive_search(monster, nested_keys)
                else:
                    filtered_monster[key] = self._recursive_search(monster, nested_keys)
            filtered_monsters.append(filtered_monster)

        return filtered_monsters
    
    def json_to_dataframe(self, keys_needed) -> DataFrame:
        self.df = json_normalize(self.filter_json(keys_needed), errors='ignore')
        return self.df

    def filter_dataframe(self, column_name, condition, value_to_compare, df: DataFrame = None) -> DataFrame:
        df_to_filter = None
        if df is not None:
            df_to_filter = df
        else:
            df_to_filter = self.df

        if not isinstance(df_to_filter, DataFrame):
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
        

        if not isinstance(df, DataFrame):
            self.df = df_to_filter

        return df_to_filter
        

    def filter_dataframe_by_type(self, column_name, value_type, df: DataFrame = None) -> DataFrame:
        df_to_filter = None
        if df is not None:
            df_to_filter = df
        else:
            df_to_filter = self.df

        if not isinstance(df_to_filter, DataFrame):
            raise ValueError("Aucune Dataframe n'a été instanciée.")
        
        filtered_df = df_to_filter[df_to_filter[column_name].apply(lambda x: type(x).__name__) == value_type]

        if not isinstance(df, DataFrame):
            self.df = filtered_df

        return filtered_df
    
    def apply_filters(self, filter_list: list, df: DataFrame = None)-> DataFrame:
        df_to_filter = None
        if df is not None:
            df_to_filter = df
        else:
            df_to_filter = self.df

        for fltr in filter_list:
            if not isinstance(fltr[0], list):
                df_to_filter = self.filter_dataframe(fltr[0], fltr[1], fltr[2], df_to_filter)
            else:
                df_list = []
                for sub_fltr in fltr:
                    df_list.append(self.filter_dataframe(sub_fltr[0], sub_fltr[1], sub_fltr[2], df_to_filter))
                df_to_filter = concat(df_list)

        if not isinstance(df, DataFrame):
            self.df = df_to_filter

        return df_to_filter
    
    def apply_type_filters(self, filter_list: list, df: DataFrame = None)-> DataFrame:
        df_to_filter = None
        if df is not None:
            df_to_filter = df
        else:
            df_to_filter = self.df

        for fltr in filter_list:
            if not isinstance(fltr[0], list):
                df_to_filter = self.filter_dataframe_by_type(fltr[0], fltr[1], df_to_filter)
            else:
                df_list = []
                for sub_fltr in fltr:
                    df_list.append(self.filter_dataframe_by_type(sub_fltr[0], sub_fltr[1], df_to_filter))
                df_to_filter = concat(df_list)

        if not isinstance(df, DataFrame):
            self.df = df_to_filter

        return df_to_filter
    
import json
import os

current_dir = os.path.dirname(__file__)
monsters_file_path = os.path.abspath(os.path.join(current_dir, '..', '..', 'data', 'monsters_mock.json'))

monsters_file = open(monsters_file_path, 'r')

monsterList = json.load(monsters_file)
monsters_file.close()

transformer = Transform(monsterList)
keys_needed = ["index", "name", "size", 'speed.walk', 'armor_class.type', 'armor_class.value', 'actions.name', 'actions.actions.count'] 

my_df = transformer.json_to_dataframe(keys_needed)

type_filters = [
    [
        "actions.name", 'list'
    ]
]

transformer.apply_type_filters(type_filters)

filters = [
    [
        ["armor_class.value", "equal_or_lower", 10],
        ["armor_class.value", "equal_or_bigger", 18]
    ],
    [
        "size", "equal", "Small"
    ],
    [
        "speed.walk", "equal", "40 ft."
    ]
]

print(transformer.apply_filters(filters))

