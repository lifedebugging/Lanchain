from langchain_community.document_loaders.csv_loader import CSVLoader
from pathlib import Path

loader = CSVLoader(file_path=r"D:\Downloads\sample-csv-files-sample-6.csv")
data = loader.load()


print(data[0].page_content)
print(data[0].metadata)
