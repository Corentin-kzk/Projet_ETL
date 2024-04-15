# Documentation du module `Transform`

Le module `Transform` est conçu pour manipuler et transformer des données JSON en utilisant la bibliothèque pandas. Il permet de filtrer, normaliser, et transformer ces données en DataFrame pour une analyse plus approfondie. Voici un guide détaillé des fonctionnalités de ce module.

## Classe et Méthodes

### Classe `Transform`

#### Méthodes

#### `__init__(self, monsterList: list)`
Constructeur de la classe `Transform`.

**Paramètres :**
- `monsterList` : liste contenant des dictionnaires. Chaque dictionnaire représente un "monstre" avec ses propriétés en format JSON.

#### `filter_json(self, keys_needed) -> dict`
Filtre les données JSON selon les clés nécessaires.

**Paramètres :**
- `keys_needed` : liste des clés (chaînes de caractères) qui déterminent quelles informations extraire des données JSON. Vous pouvez accéder aux clés imbriquées grace au séparateur ```.``` (point).
###### Exemple : 
```['name', 'armor_class.type']```

**Retour :**
- Liste de dictionnaires avec les données filtrées.


#### `_recursive_search(self, nested_dict, keys)`
Cherche récursivement des valeurs dans un dictionnaire selon une liste de clés.

**Paramètres :**
- `nested_dict` : dictionnaire dans lequel effectuer la recherche.
- `keys` : liste de clés pour la recherche récursive.

**Retour :**
- Résultat de la recherche; peut être une liste, une valeur unique ou `None` si la donnée n'existe pas.

#### `json_to_dataframe(self, keys_needed) -> DataFrame`
Convertit les données JSON filtrées en DataFrame pandas.

**Paramètres :**
- `keys_needed` : liste des clés nécessaires pour filtrer les données avant la conversion.

**Retour :**
- DataFrame contenant les données filtrées.

#### `filter_dataframe(self, column_name, condition, value_to_compare, df=None) -> DataFrame`
Filtre un DataFrame basé sur des conditions spécifiques.

**Paramètres :**
- `column_name` : nom de la colonne à filtrer.
- `condition` : condition de filtrage ('equal', 'bigger', 'lower', 'equal_or_bigger', 'equal_or_lower').
- `value_to_compare` : valeur à comparer. Si la valeur est une liste, c'est sa taille qui est comparée.
- `df` : DataFrame optionnel à filtrer; si non spécifié, le DataFrame actuel est utilisé.

**Retour :**
- DataFrame filtré.

#### `filter_dataframe_by_type(self, column_name, value_type, df=None) -> DataFrame`
Filtre un DataFrame en fonction du type de données d'une colonne.

**Paramètres :**
- `column_name` : nom de la colonne à vérifier.
- `value_type` : type de données à filtrer (par exemple, 'list', 'str', etc.).
- `df` : DataFrame optionnel à filtrer; si non spécifié, le DataFrame actuel est utilisé.

**Retour :**
- DataFrame filtré selon le type spécifié.

#### `apply_filters(self, filter_list, df=None) -> DataFrame`
Applique une série de filtres au DataFrame.

**Paramètres :**
- `filter_list` : liste de filtres à appliquer.
- `df` : DataFrame optionnel sur lequel appliquer les filtres; si non spécifié, le DataFrame actuel est utilisé.

**Retour :**
- DataFrame après l'application des filtres.

#### `apply_type_filters(self, filter_list, df=None) -> DataFrame`
Applique des filtres basés sur le type de données aux colonnes spécifiées du DataFrame.

**Paramètres :**
- `filter_list` : liste de filtres de type à appliquer.
- `df` : DataFrame optionnel à filtrer; si non spécifié, le DataFrame actuel est utilisé.

**Retour :**
- DataFrame après l'application des filtres de type.

## Exemples d'utilisation

### Initialisation et chargement des données
```python
import json
from transform import Transform

# Charger les données JSON depuis un fichier
with open('monsters.json', 'r') as file:
    monster_list = json.load(file)

# Initialisation de l'objet Transform
transformer = Transform(monsterList=monster_list)
```

### Conversion de JSON en DataFrame
```python
keys_needed = ["name", "size", "speed.walk", "armor_class.type", "armor_class.value"]
df = transformer.json_to_dataframe(keys_needed)
print(df.head())
```

### Application de filtres simples
```python
filtered_df = transformer.filter_dataframe(column_name="armor_class.value", condition="bigger", value_to_compare=10)
print(filtered_df.head())
```

### Application de filtres complexes
```python
filters =   [    
                [
                    ["armor_class.value", "equal_or_lower", 10], # dans ce cas, on applique l'opérateur AND pour avoir que les valeurs inférieures ou égale à 1O et supérieures ou égale à 18
                    ["armor_class.value", "equal_or_bigger", 18]
                ],
                ["size", "equal", "Large"]
            ]

result_df = transformer.apply_filters(filters)
print(result_df.head())
```


### Application de filtres de Type simple

```python
# Supposons que vous voulez filtrer toutes les lignes où la colonne 'armor_class.value' contient un entier
filtered_by_type_df = transformer.filter_dataframe_by_type(column_name="armor_class.value", value_type="int")
print(filtered_by_type_df.head())
```

### Application de filtres de Type complexe
```python
# Supposons que vous souhaitez appliquer plusieurs filtres de type
type_filters = [
    [
        ["armor_class.value", "int"], # dans ce cas, on applique l'opérateur AND pour avoir que les valeurs de type entier et de type list
        ["armor_class.value", "list"]
    ],
    ["speed.walk", "str"]
]

filtered_df = transformer.apply_type_filters(type_filters)
print(filtered_df.head())
```
