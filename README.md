# ETL - EEM
This project is an example implementation of an ETL (Extract, Transform, Load) process using Python and PDM (Python Development Master) for dependency management.

## Description
The ETL process is commonly used in computer science to extract data from data sources, transform it as needed, and then load it into another database or data warehouse.

This project presents a simple ETL process with the following features:

- Data extraction from a data source (e.g., a CSV file).
- Data transformation by applying cleaning, manipulation, or enrichment operations.
- Loading transformed data into a database or another storage system.

## Prerequisites
Before getting started, ensure you have Python and PDM (Python Development Master) installed. You can install PDM using pip:

```bash
pip install pdm
```

## Installing Dependencies
After cloning this repository, you can install the necessary dependencies by running the following command:

```bash
pdm sync
```

This will install all dependencies specified in the `pyproject.toml` file.

## Project Structure
The project structure is as follows:

```
.
├── data/
│   ├── data.csv            # CSV file as data source
│   └── data.json           # JSON file as data source
├── main.py                 # Python script for the ETL process
│
├── services/               # Services folder containing dynamic ETL
│   ├── core                
│   ├── extract             
│   ├── transform
│   └── load 
│
├── modules/                # Module folder containing Mini ETL for data serialization
│   ├── listDetails/        # Retrieves monster details
│   │   ├── extract         
│   │   ├── transform
│   │   └── load 
│   │
│   └── listIndex/          # Retrieves monsters
│       ├── extract             
│       ├── transform
│       └── load 
│   
├── pyproject.toml          # PDM configuration file
├── README.md               # This README file
└── requirements.txt        # List of project dependencies (for reference)

```

## Usage
To execute the ETL process, you can specify instructions using a YAML file with the `-y` flag. Here's an example YAML file:


Then, you can run the `main.py` script with this YAML file.

```bash
pdm run src/main.py -y instructions.yml
```

Make sure your environment is properly configured and all dependencies are installed.

# Documentation of the `Extract` Module

The `Extract` module is designed to extract JSON, CSV, and API data using the pandas library. It extracts and transforms this data into DataFrame. Here's a detailed guide to the features of this module.

## Functions

### `def get_api(path: str) -> JsonResponse`
Extracts data from an API and returns JSON.

**Parameters:**
- `path`: API URL passed via YAML.

**Returns:**
- JSON response from the API.

### `def get_csv(path) -> DataFrame`
Extracts data from a CSV and returns a DataFrame.

**Parameters:**
- `path`: URL of the file passed via YAML.

**Returns:**
- Returns a DataFrame corresponding to the CSV data.

### `def get_Json(path: str) -> JsonResponse`
Extracts data from a JSON file and returns a DataFrame.

**Parameters:**
- `path`: URL of the JSON file passed via YAML.

**Returns:**
- Returns a DataFrame corresponding to the JSON data.

## Usage Examples

### JSON:
```yaml
# ETL Instructions
EXTRACT :
  your_key :
    json : './src/data/monsters.json'
```

### CSV:
```yaml
# ETL Instructions
EXTRACT :
  your_key :
    csv : './src/data/monsters.csv'
```

### API:
```yaml
# ETL Instructions
EXTRACT :
  your_key :
    api : 'https://api.monsters/'
```

# Documentation of the `Transform` Module

The `Transform` module is designed to manipulate and transform JSON data using the pandas library. It allows filtering, normalization, and transformation of this data into a DataFrame for further analysis. Here's a detailed guide to the features of this module.

## Functions

### `filter_json(monsterList: list, keys_needed: list) -> dict`
Filters JSON data according to the required keys.

**Parameters:**
- `monsterList`: list containing dictionaries. Each dictionary represents a "monster" with its properties in JSON format.
- `keys_needed`: list of keys (strings) that determine which information to extract from the JSON data. You can access nested keys using the `.` (dot) separator. **Example:** ```['name', 'armor_class.type']```

**Returns:**
- List of dictionaries with filtered data.

### `recursive_search(nested_dict, keys)`
Recursively searches for values in a dictionary according to a list of keys.

**Parameters:**
- `nested_dict`: dictionary to perform the search on.
- `keys`: list of keys for recursive search.

**Returns:**
- Search result; can be a list, a single value, or `None` if the data does not exist.

### `json_to_dataframe(monsterList: list, keys_needed: list) -> DataFrame`
Converts filtered JSON data into a pandas DataFrame.

**Parameters:**
- `monsterList`: list containing dictionaries. Each dictionary represents a "monster" with its properties in JSON format.
- `keys_needed`: list of required keys to filter the data before conversion.

**Returns:**
- DataFrame containing the filtered data.

### `filter_dataframe(df: DataFrame, column_name: str, condition: str, value_to_compare) -> DataFrame`
Filters a DataFrame based on specific conditions.

**Parameters:**
- `df`: DataFrame to filter.
- `column_name`: name of the column to filter.
- `condition`: filtering condition ('equal', 'bigger', 'lower', 'equal_or_bigger', 'equal_or_lower').
- `value_to_compare`: value to compare. If the value is a list, its size is compared.

**Returns:**
- Filtered DataFrame.

### `filter_dataframe_by_type(df: DataFrame, column_name: str, value_type: str) -> DataFrame`
Filters a DataFrame based on the data type of a column.

**Parameters:**
- `df`: DataFrame to filter.
- `column_name`: name of the column to check.
- `value_type`: data type to filter (e.g., 'list', 'str', etc.).

**Returns:**
- DataFrame filtered according to the specified type.

### `apply_filters(df: DataFrame, filter_list: list) -> DataFrame`
Applies a series of filters to the DataFrame.

**Parameters:**
- `df`: DataFrame on which to apply the filters.
- `filter_list`: list of filters to apply.

**Returns:**
- DataFrame after applying the filters.

### `apply_type_filters(df: DataFrame, filter_list: list) -> DataFrame`
Applies filters based on data type to the specified columns of the DataFrame.

**Parameters:**
- `df`: DataFrame to filter; if not specified, the current DataFrame is used.
- `filter_list`: list of type filters to apply.

**Returns:**
- DataFrame after applying type filters.

## Usage Examples

### Initializing and Loading Data
```python
import json
from transform import filter_json, json_to_dataframe

# Load JSON data from a file
with open('monsters.json', 'r') as file:
    monster_list = json.load(file)

# Filter JSON data
keys_needed = ["name", "size", "speed.walk", "armor_class.type", "armor_class.value"]

# Convert JSON to DataFrame keeping only the desired fields
df = json_to_dataframe(monster_list, keys_needed)
print(df.head())
```

### Applying Simple Filters
```python
from transform import filter_dataframe

# Filter the DataFrame
filtered_df = filter_dataframe("armor_class.value", "bigger", 10, df)
print(filtered_df.head())
```

### Applying Complex Filters
```python
from transform import apply_filters

filters =   [    
                [
                    ["armor_class.value", "equal_or_lower", 10], # in this case, we apply the AND operator to have only values lower or equal to 1O and higher or equal to 18
                    ["armor_class.value", "equal_or_bigger", 18]
                ],
                ["size", "equal", "Large"]
            ]

result_df = apply_filters(filters, df)
print(result_df.head())
```

### Applying Simple Type Filters

```python
from transform import filter_dataframe_by_type

# Filter the DataFrame by type
filtered_by_type_df = filter_dataframe_by_type(df, "armor_class.value", "int")
print(filtered_by_type_df.head())
```

### Applying Complex Type Filters
```python
from transform import apply_type_filters

# Suppose you want to apply multiple type filters
type_filters = [
    [
        ["armor_class.value", "int"], # in this case, we apply the AND operator to have only integer and list type values
        ["armor_class.value", "list"]
    ],
    ["speed.walk", "str"]
]

filtered_df = apply_type_filters(df, type_filters)
print(filtered_df.head())
```

## YAML File for the TRANSFORM Part:

```yaml
# TRANSFORM Part of YAML configuration for processing monster data
TRANSFORM:
  monster:
    # List of keys needed to extract from the initial JSON
    keys_needed:
      - 'index'               
      - 'name'                
      - 'size'                          # Possible values: 'Tiny', 'Small', 'Medium', and 'Large'
      - 'speed.walk'          
      - 'armor_class.type'    
      - 'armor_class.value'   
      - 'actions.name'        
      - 'actions.actions.action_name'  

    # Filters data based on the type of certain columns
    filter_by_type:
      - - 'index'             # Index must be of string type
        - 'str'
      - - - 'armor_class.value'  # Armor value can be of list type
          - 'list'
        - - 'armor_class.value'  # or integer type
          - 'int'

    # Applies filters on data based on specific conditions
    filter_by:
      - - 'size'              # Size must be equal to 'Large'
        - 'equal'
        - 'Large'
      - - 'speed.walk'        # Walking speed must be equal to '40 ft.'
        - 'equal'
        - '40 ft.'
      - - - 'armor_class.value'  # Armor value must be lower or equal to 10
          - 'equal_or_lower'
          - 10
        - - 'armor_class.value'  # and higher or equal to 18
          - 'equal_or_bigger'
          - 18

    # Sets the sorting order of transformed data
    order: 'ASC'              # Sorting in ascending order
```

# Documentation of the `LOAD` Module

The `LOAD` module is designed to load Extracted and Transformed data into the following file types: JSON, CSV using the pandas library. Here's a detailed guide to the features of this module.

## Functions

### `def load_csv(fileName,df: DataFrame):`
Extracts data from a DataFrame and returns a CSV file.

**Parameters:**
- `fileName`: File name
- `df`: DataFrame 

**Returns:**
- void

### `def load_json(fileName,df: DataFrame):`
Extracts data from a DataFrame and returns a JSON file.

**Parameters:**
- `fileName`: File name
- `df`: DataFrame 

**Returns:**
- Void

## Usage Examples

## Loading data as JSON and CSV:
```yaml
# ETL Instructions
LOAD:
   monster :
    json : 'filtered_monsters'
    csv : 'filtered_monsters'
```

## Loading data as CSV:
```yaml
# ETL Instructions
LOAD:
   monster :
    csv : 'filtered_monsters'
```

## Loading data as JSON:
```yaml
# ETL Instructions
LOAD:
   monster :
    json : 'filtered_monsters'
```

## Authors

- [Corentin KOZKA](https://github.com/Corentin-kzk) - Developer
- [Frederick VU](https://github.com/kohai-fred) - Developer
- [Youva IBRAHIM](https://github.com/YouvaIBRAHIM) - Developer

## License

This project is licensed under CC-BY-NC-ND - see the [LICENSE](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.en) file for more details.
``` ````