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

    
monster = {
  "index": "aboleth",
  "name": "Aboleth",
  "size": "Large",
  "type": "aberration",
  "alignment": "lawful evil",
  "armor_class": [
    {
      "type": "natural",
      "value": 17
    }
  ],
  "hit_points": 135,
  "hit_dice": "18d10",
  "hit_points_roll": "18d10+36",
  "speed": {
    "walk": "10 ft.",
    "swim": "40 ft."
  },
  "strength": 21,
  "dexterity": 9,
  "constitution": 15,
  "intelligence": 18,
  "wisdom": 15,
  "charisma": 18,
  "proficiencies": [
    {
      "value": 6,
      "proficiency": {
        "index": "saving-throw-con",
        "name": "Saving Throw: CON",
        "url": "/api/proficiencies/saving-throw-con"
      }
    },
    {
      "value": 8,
      "proficiency": {
        "index": "saving-throw-int",
        "name": "Saving Throw: INT",
        "url": "/api/proficiencies/saving-throw-int"
      }
    }
  ],
  "damage_vulnerabilities": [],
  "damage_resistances": [],
  "damage_immunities": [],
  "condition_immunities": [],
  "senses": {
    "darkvision": "120 ft.",
    "passive_perception": 20
  },
  "languages": "Deep Speech, telepathy 120 ft.",
  "challenge_rating": 10,
  "proficiency_bonus": 4,
  "xp": 5900,
  "special_abilities": [
    {
      "name": "Amphibious",
      "desc": "The aboleth can breathe air and water."
    },
    {
      "name": "Mucous Cloud",
      "desc": "While underwater, the aboleth is surrounded by transformative mucus. A creature that touches the aboleth or that hits it with a melee attack while within 5 ft. of it must make a DC 14 Constitution saving throw. On a failure, the creature is diseased for 1d4 hours. The diseased creature can breathe only underwater.",
      "dc": {
        "dc_type": {
          "index": "con",
          "name": "CON",
          "url": "/api/ability-scores/con"
        },
        "dc_value": 14,
        "success_type": "none"
      }
    },
    {
      "name": "Probing Telepathy",
      "desc": "If a creature communicates telepathically with the aboleth, the aboleth learns the creature's greatest desires if the aboleth can see the creature."
    }
  ],
  "actions": [
    {
      "name": "Multiattack",
      "multiattack_type": "actions",
      "desc": "The aboleth makes three tentacle attacks.",
      "actions": [
        {
          "action_name": "Tentacle",
          "count": 3,
          "type": "melee"
        },
        {
          "action_name": "Tentacle",
          "count": 4,
          "type": "melee"
        }
      ]
    },
    {
      "multiattack_type": "actions",
      "desc": "The aboleth makes three tentacle attacks.",
      "actions": [
        {
          "action_name": "Test",
          "count": 3,
          "type": "melee"
        }
      ]
    }
  ],
  "legendary_actions": [
    {
      "name": "Detect",
      "desc": "The aboleth makes a Wisdom (Perception) check."
    },
    {
      "name": "Tail Swipe",
      "desc": "The aboleth makes one tail attack."
    },
    {
      "name": "Psychic Drain (Costs 2 Actions)",
      "desc": "One creature charmed by the aboleth takes 10 (3d6) psychic damage, and the aboleth regains hit points equal to the damage the creature takes.",
      "attack_bonus": 0,
      "damage": [
        {
          "damage_type": {
            "index": "psychic",
            "name": "Psychic",
            "url": "/api/damage-types/psychic"
          },
          "damage_dice": "3d6"
        }
      ]
    }
  ],
  "image": "/api/images/monsters/aboleth.png",
  "url": "/api/monsters/aboleth"
}


monsterList = [monster] 
transformer = Transform(monsterList)
keys_needed = ["index", "name", "size", "actions.actions", "actions.name", "special_abilities.name"] 
filtered_monsters = transformer.filter(keys_needed)
print(filtered_monsters)