# CSVLoader

One of the common used document loader for CSV files.

Import : `from langchain_community.document_loaders.csv_loade`r import `CSVLoader`

# Syntax :
```
loader = CSVLoader(file_path="...")
data =loader.load()
```
yup that's it.

# Observation :
1. when you print `data[0].page_content`it will fetch the data in that row.
2. `print(data[0].metadata)` this will show source along with row for example data[0] = 'row' : 0
