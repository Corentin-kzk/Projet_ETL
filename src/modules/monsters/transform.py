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

            return result if len(result) > 1 else value

        return self._recursive_search(nested_dict.get(keys[0]), keys[1:])

    def filter(self, keys_needed):
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
    
    def json_to_dataframe(self, keys_needed):
        return pd.json_normalize(self.filter(keys_needed), errors='ignore')

    
import json
import os

current_dir = os.path.dirname(__file__)
monsters_file_path = os.path.abspath(os.path.join(current_dir, '..', '..', 'data', 'monsters_mock.json'))

monsters_file = open(monsters_file_path, 'r')

monsterList = json.load(monsters_file)
transformer = Transform(monsterList)
keys_needed = ["index", "name", "size", 'armor_class.type', 'actions.name', 'actions.actions.action_name', 'actions.actions.count'] 

print(transformer.json_to_dataframe(keys_needed))
monsters_file.close()
