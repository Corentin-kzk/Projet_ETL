import pandas as pd
class Transform:
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
            for item in nested_dict.get(keys[0]):
                value = self._recursive_search(item, keys[1:])
                result.append(value)

            return result

        return {keys[1:][0]: self._recursive_search(nested_dict.get(keys[0]), keys[1:])}

    def format(self, keys_needed):
        filtered_monsters = []

        for monster in self.monsterList:
            filtered_monster = {}
            for key in keys_needed:
                nested_keys = key.split('.')
                if nested_keys[0] not in filtered_monster:
                    filtered_monster[nested_keys[0]] = {}
                if len(nested_keys) > 1:
                    if nested_keys[1] not in filtered_monster[nested_keys[0]]:
                        filtered_monster[nested_keys[0]][nested_keys[1]] = self._recursive_search(monster, nested_keys)
                else:
                    filtered_monster[nested_keys[0]] = self._recursive_search(monster, nested_keys)
            filtered_monsters.append(filtered_monster)

        return filtered_monsters
    
    def filter_v2(self, keys_needed):
        metas = []
        records = []
        for val in keys_needed:
            splitted_val = val.split('.')
            if len(splitted_val) > 1: 
                records.append(splitted_val)
            else:
                metas.append(val)
        
        df_list = []
    
        print(self.format(keys_needed))
        if len(records) > 0:
            for record in records:
                df_list.append(pd.json_normalize([{'index': 'aboleth', 'name': 'Aboleth', 'size': 'Large', 'armor_class.type': 'natural', 'armor_class.value': 17}], record_prefix=".".join(record[:-1]) + ".", meta=metas, errors='ignore'))
        else:
            df_list.append(pd.json_normalize(self.format(keys_needed), meta=keys_needed, errors='ignore'))
        return pd.concat(df_list, ignore_index=True)

    
import json
import os

current_dir = os.path.dirname(__file__)
monsters_file_path = os.path.abspath(os.path.join(current_dir, '..', '..', 'data', 'monsters_mock.json'))

monsters_file = open(monsters_file_path, 'r')

monsterList = json.load(monsters_file)
transformer = Transform(monsterList)
keys_needed = ["index", "name", "size", 'armor_class.type'] 



print(transformer.filter_v2(keys_needed))
monsters_file.close()
