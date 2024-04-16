# Documentation du module `Transform`

Le module `Transform` est conçu pour manipuler et transformer des données JSON en utilisant la bibliothèque pandas. Il permet de filtrer, normaliser, et transformer ces données en DataFrame pour une analyse plus approfondie. Voici un guide détaillé des fonctionnalités de ce module.

## Fonctions

### `filter_json(monsterList: list, keys_needed: list) -> dict`
Filtre les données JSON selon les clés nécessaires.

**Paramètres :**
- `monsterList` : liste contenant des dictionnaires. Chaque dictionnaire représente un "monstre" avec ses propriétés en format JSON.
- `keys_needed` : liste des clés (chaînes de caractères) qui déterminent quelles informations extraire des données JSON. Vous pouvez accéder aux clés imbriquées grâce au séparateur `.` (point). **Exemple :** ```['name', 'armor_class.type']```


**Retour :**
- Liste de dictionnaires avec les données filtrées.

### `recursive_search(nested_dict, keys)`
Cherche récursivement des valeurs dans un dictionnaire selon une liste de clés.

**Paramètres :**
- `nested_dict` : dictionnaire dans lequel effectuer la recherche.
- `keys` : liste de clés pour la recherche récursive.

**Retour :**
- Résultat de la recherche; peut être une liste, une valeur unique ou `None` si la donnée n'existe pas.

### `json_to_dataframe(monsterList: list, keys_needed: list) -> DataFrame`
Convertit les données JSON filtrées en DataFrame pandas.

**Paramètres :**
- `monsterList` : liste contenant des dictionnaires. Chaque dictionnaire représente un "monstre" avec ses propriétés en format JSON.
- `keys_needed` : liste des clés nécessaires pour filtrer les données avant la conversion.

**Retour :**
- DataFrame contenant les données filtrées.

### `filter_dataframe(df: DataFrame, column_name: str, condition: str, value_to_compare) -> DataFrame`
Filtre un DataFrame basé sur des conditions spécifiques.

**Paramètres :**
- `df` : DataFrame à filtrer.
- `column_name` : nom de la colonne à filtrer.
- `condition` : condition de filtrage ('equal', 'bigger', 'lower', 'equal_or_bigger', 'equal_or_lower').
- `value_to_compare` : valeur à comparer. Si la valeur est une liste, c'est sa taille qui est comparée.

**Retour :**
- DataFrame filtré.

### `filter_dataframe_by_type(df: DataFrame, column_name: str, value_type: str) -> DataFrame`
Filtre un DataFrame en fonction du type de données d'une colonne.

**Paramètres :**
- `df` : DataFrame à filtrer.
- `column_name` : nom de la colonne à vérifier.
- `value_type` : type de données à filtrer (par exemple, 'list', 'str', etc.).

**Retour :**
- DataFrame filtré selon le type spécifié.

### `apply_filters(df: DataFrame, filter_list: list) -> DataFrame`
Applique une série de filtres au DataFrame.

**Paramètres :**
- `df` : DataFrame sur lequel appliquer les filtres.
- `filter_list` : liste de filtres à appliquer.

**Retour :**
- DataFrame après l'application des filtres.

### `apply_type_filters(df: DataFrame, filter_list: list) -> DataFrame`
Applique des filtres basés sur le type de données aux colonnes spécifiées du DataFrame.

**Paramètres :**
- `df` : DataFrame à filtrer; si non spécifié, le DataFrame actuel est utilisé.
- `filter_list` : liste de filtres de type à appliquer.

**Retour :**
- DataFrame après l'application des filtres de type.

## Exemples d'utilisation

### Initialisation et chargement des données
```python
import json
from transform import filter_json, json_to_dataframe

# Charger les données JSON depuis un fichier
with open('monsters.json', 'r') as file:
    monster_list = json.load(file)

# Filtrer les données JSON
keys_needed = ["name", "size", "speed.walk", "armor_class.type", "armor_class.value"]

# Convertir le JSON en DataFrame en gardant seulement les champs souhaités
df = json_to_dataframe(monster_list, keys_needed)
```

### Application de filtres simples
```python
from transform import filter_dataframe

# Filtrer le DataFrame
filtered_df = filter_dataframe("armor_class.value", "bigger", 10, df)
```

### Application de filtres complexes
```python
from transform import apply_filters

filters =   [    
                [
                    ["armor_class.value", "equal_or_lower", 10], # dans ce cas, on applique l'opérateur AND pour avoir que les valeurs inférieures ou égale à 1O et supérieures ou égale à 18
                    ["armor_class.value", "equal_or_bigger", 18]
                ],
                ["size", "equal", "Large"]
            ]

result_df = apply_filters(filters, df)
```

### Application de filtres de Type simple

```python
from transform import filter_dataframe_by_type

# Filtrer le DataFrame par type
filtered_by_type_df = filter_dataframe_by_type(df, "armor_class.value", "int")
```

### Application de filtres de Type complexes
```python
from transform import apply_type_filters

# Supposons que vous souhaitez appliquer plusieurs filtres de type
type_filters = [
    [
        ["armor_class.value", "int"], # dans ce cas, on applique l'opérateur AND pour avoir que les valeurs de type entier et de type list
        ["armor_class.value", "list"]
    ],
    ["speed.walk", "str"]
]

filtered_df = apply_type_filters(df, type_filters)
```

## Le fichier YAML pour la partie TRANSFORM :

```yaml
# Partie TRANSFORM de la configuration YAML pour le traitement des données de monstres
TRANSFORM:
  monster:
    # Liste des clés nécessaires à extraire du JSON initial
    keys_needed:
      - 'index'               
      - 'name'                
      - 'size'                          # Valeurs possibles : 'Tiny', 'Small', 'Medium' et 'Large'
      - 'speed.walk'          
      - 'armor_class.type'    
      - 'armor_class.value'   
      - 'actions.name'        
      - 'actions.actions.action_name'  

    # Filtre les données selon le type de certaines colonnes
    filter_by_type:
      - - 'index'             # L'index doit être de type chaîne de caractères
        - 'str'
      - - - 'armor_class.value'  # La valeur de l'armure peut être de type liste
          - 'list'
        - - 'armor_class.value'  # ou de type entier
          - 'int'

    # Applique des filtres sur les données selon des conditions spécifiques
    filter_by:
      - - 'size'              # Taille doit être égale à 'Large'
        - 'equal'
        - 'Large'
      - - 'speed.walk'        # La vitesse de marche doit être égale à '40 ft.'
        - 'equal'
        - '40 ft.'
      - - - 'armor_class.value'  # Valeur de l'armure doit être inférieure ou égale à 10
          - 'equal_or_lower'
          - 10
        - - 'armor_class.value'  # et supérieure ou égale à 18
          - 'equal_or_bigger'
          - 18

    # Définit l'ordre de tri des données transformées
    order: 'ASC'              # Tri en ordre ascendant
```

