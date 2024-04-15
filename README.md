# ETL - EEM
This project is an example implementation of an ETL (Extract, Transform, Load) process using Python and PDM (Python Development Master) for dependency management.

## Description

The ETL process is commonly used in computer science to extract data from data sources, transform it as needed, and then load it into another database or data warehouse.

This project demonstrates a simple ETL process with the following features:

- Data extraction from a data source (e.g., a CSV file).
- Data transformation by applying cleaning, manipulation, or enrichment operations.
- Loading transformed data into a database or another storage system.

## Prerequisites

Before getting started, make sure you have Python and PDM (Python Development Master) installed. You can install PDM using pip:

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
│   └── data.csv           # CSV file as data source
├── src/
│   └── main.py             # Python script for the ETL process
├── pyproject.toml          # PDM configuration file
├── README.md               # This README file
└── requirements.txt        # List of project dependencies (for reference)
```

## Usage

To execute the ETL process, you can specify instructions using a YAML file using the `-y` flag. Here's an example YAML file:

```yaml
# ETL Instructions
source:
  type: csv
  path: data/input.csv
transformations:
  - name: clean_data
    type: cleaning
  - name: enrich_data
    type: enrichment
destination:
  type: database
  connection_string: "your_database_connection_string"
```

Then, you can execute the `etl_script.py` script with this YAML file using PDM:

```bash
pdm run src/main.py -y instructions.yml
```

Make sure your environment is properly configured and all dependencies are installed.

## Authors

- [Corentin KOZKA](https://github.com/Corentin-kzk) - Developer
- [Frederick Vu](https://github.com/Corentin-kzk) - Developer
- [Youva IBRAHIM](https://github.com/YouvaIBRAHIM) - Developer

## License

This project is licensed under the CC-BY-NC-ND - see the [LICENSE](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.en) file for details.
