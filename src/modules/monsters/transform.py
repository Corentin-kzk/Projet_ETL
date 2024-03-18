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

    def filter(self, keys_needed):
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

    
import json
import os

current_dir = os.path.dirname(__file__)
monsters_file_path = os.path.abspath(os.path.join(current_dir, '..', '..', 'data', 'monsters_mock.json'))

monsters_file = open(monsters_file_path, 'r')

monsterList = json.load(monsters_file)
transformer = Transform(monsterList)
keys_needed = ["index", "name", "size", "actions.actions", "actions.name", "special_abilities.dc.dc_type.name"] 
filtered_monsters = transformer.filter(keys_needed)
print(filtered_monsters)


monsters_file.close()