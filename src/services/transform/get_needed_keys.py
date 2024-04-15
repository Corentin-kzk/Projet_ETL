from pandas import DataFrame, json_normalize
import json

def get_needed_keys(data, directives):
    monster_list = json.loads(data.get().to_json(orient="records"))
    new_value = json_to_dataframe(monster_list, directives)
    data.set(new_value)


def recursive_search(nested_dict, keys):
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
            value = recursive_search(item, keys[1:])
            result.append(value)

        return result if len(result) > 1 else value

    return recursive_search(nested_dict.get(keys[0]), keys[1:])

def filter_json(monsterList, keys_needed) -> dict:
    filtered_monsters = []

    for monster in monsterList:
        filtered_monster = {}
        for key in keys_needed:
            nested_keys = key.split('.')
            if key not in filtered_monster:
                filtered_monster[key] = {}
            if len(nested_keys) > 1:
                if nested_keys[1] not in filtered_monster[key]:
                    filtered_monster[key] = recursive_search(monster, nested_keys)
            else:
                filtered_monster[key] = recursive_search(monster, nested_keys)
        filtered_monsters.append(filtered_monster)

    return filtered_monsters

def json_to_dataframe(monsterList, keys_needed) -> DataFrame:
    df = json_normalize(filter_json(monsterList, keys_needed), errors='ignore')
    return df