# ETL - EEM
Ce projet est un exemple d'implémentation d'un processus ETL (Extract, Transform, Load) en utilisant Python et PDM (Python Development Master) pour la gestion des dépendances.

## Description

Le processus ETL est couramment utilisé en informatique pour extraire des données de sources de données, les transformer au besoin, puis les charger dans une autre base de données ou un entrepôt de données.

Ce projet présente un processus ETL simple avec les fonctionnalités suivantes :

- Extraction de données à partir d'une source de données (par exemple, un fichier CSV).
- Transformation des données en appliquant des opérations de nettoyage, de manipulation ou d'enrichissement.
- Chargement des données transformées dans une base de données ou un autre système de stockage.

## Prérequis

Avant de commencer, assurez-vous d'avoir Python et PDM (Python Development Master) installés. Vous pouvez installer PDM en utilisant pip :

```bash
pip install pdm
```

## Installation des dépendances

Après avoir cloné ce dépôt, vous pouvez installer les dépendances nécessaires en exécutant la commande suivante :

```bash
pdm sync
```

Cela installera toutes les dépendances spécifiées dans le fichier `pyproject.toml`.

## Structure du projet

La structure du projet est la suivante :

```
.
├── data/
│   ├── data.csv            # Fichier CSV en tant que source de données
│   └── data.json           # Fichier JSON en tant que source de données
├── main.py                 # Script Python pour le processus ETL
│
├── services/               # Dossier Services contenant l'ETL dynamique
│   ├── core                
│   ├── extract             
│   ├── transform
│   └── load 
│
├── modules/                # Dossier Module contenant des Mini ETL pour la sérialisation des données
│   ├── listDetails/        # Permet de récupérer les détails des monstres
│   │   ├── extract         
│   │   ├── transform
│   │   └── load 
│   │
│   └── listIndex/          # Permet de récupérer les monstres
│       ├── extract             
│       ├── transform
│       └── load 
│   
├── pyproject.toml          # Fichier de configuration PDM
├── README.md               # Ce fichier README
└── requirements.txt        # Liste des dépendances du projet (pour référence)

```

## Utilisation

Pour exécuter le processus ETL, vous pouvez spécifier des instructions en utilisant un fichier YAML avec le drapeau `-y`. Voici un exemple de fichier YAML :


Ensuite, vous pouvez exécuter le script `main.py` avec ce fichier YAML.

```bash
pdm run src/main.py -y instructions.yml
```

Assurez-vous que votre environnement est correctement configuré et que toutes les dépendances sont installées.

# Documentation du module `Extract`

Le module `Extract` est conçu pour extraire des données JSON, CSV et API en utilisant la bibliothèque pandas. Il permet d'extraire et transformer ces données en DataFrame. Voici un guide détaillé des fonctionnalités de ce module.

## Fonctions

### `def get_api(path: str) -> JsonResponse`
Extrait les données d'une API et renvoie du JSON.

**Paramètres :**
- `path` : URL de l'api passé via le yaml.

**Retour :**
- Response Json de l'api.

### `def get_csv(path) -> DataFrame`
Extrait les données d'un CSV et renvoie un DataFrame.

**Paramètres :**
- `path` : URL du fichier passé via le yaml.

**Retour :**
- Retourne un DataFrame correspondant au données du csv.

### `def get_Json(path: str) -> JsonResponse`
Extrait les données d'un fichier JSON et renvoie un DataFrame.

**Paramètres :**
- `path` : URL du fichier JSON passé via le yaml.

**Retour :**
- Retourne un DataFrame correspondant au données du JSON.

## Exemples d'utilisation

## JSON :
```yaml
# ETL Instructions
EXTRACT :
  your_key :
    json : './src/data/monsters.json'
```

## CSV :
```yaml
# ETL Instructions
EXTRACT :
  your_key :
    csv : './src/data/monsters.csv'
```

## API :
```yaml
# ETL Instructions
EXTRACT :
  your_key :
    api : 'https://api.monsters/'
```

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
print(df.head())
```

### Application de filtres simples
```python
from transform import filter_dataframe

# Filtrer le DataFrame
filtered_df = filter_dataframe("armor_class.value", "bigger", 10, df)
print(filtered_df.head())
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
print(result_df.head())
```

### Application de filtres de Type simple

```python
from transform import filter_dataframe_by_type

# Filtrer le DataFrame par type
filtered_by_type_df = filter_dataframe_by_type(df, "armor_class.value", "int")
print(filtered_by_type_df.head())
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
print(filtered_df.head())
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

# Documentation du module `LOAD`

Le module `LOAD` est conçu pour charger des données Extraites et Transformées dans les types de fichiers suivants : JSON, CSV en utilisant la bibliothèque pandas. Voici un guide détaillé des fonctionnalités de ce module.

## Fonctions

### `def load_csv(fileName,df: DataFrame):`
Extrait les données d'un DataFrame et renvoie un fichier CSV.

**Paramètres :**
- `fileName` : Nom du fichier
- `df` : DataFrame 

**Retour :**
- void

### `def load_json(fileName,df: DataFrame):`
Extrait les données d'un DataFrame et renvoie un fichier JSON.

**Paramètres :**
- `fileName` : Nom du fichier
- `df` : DataFrame 

**Retour :**
- Void

## Exemples d'utilisation

## Chargement des data sous forme de JSON et de CSV :
```yaml
# ETL Instructions
LOAD:
   monster :
    json : 'filtred_monsters'
    csv : 'filtred_monsters'
```

## Chargement des data sous forme de CSV :
```yaml
# ETL Instructions
LOAD:
   monster :
    csv : 'filtred_monsters'
```

## Chargement des data sous forme de JSON :
```yaml
# ETL Instructions
LOAD:
   monster :
    json : 'filtred_monsters'
```

## Auteurs

- [Corentin KOZKA](https://github.com/Corentin-kzk) - Développeur
- [Frederick VU](https://github.com/kohai-fred) - Développeur
- [Youva IBRAHIM](https://github.com/YouvaIBRAHIM) - Développeur

## Licence

Ce projet est sous licence CC-BY-NC-ND - voir le fichier [LICENSE](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.en) pour plus de détails.
