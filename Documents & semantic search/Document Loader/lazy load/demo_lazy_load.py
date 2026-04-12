from langchain_community.document_loaders.csv_loader import CSVLoader
from pathlib import Path

loader = CSVLoader(
    file_path=r"D:\Downloads\sample-csv-files-sample-6.csv",
    csv_args={
        "delimiter" : ",",
        "fieldnames" : ["First_name", "Last_name"],
    }
)

data = loader.lazy_load()

for doc in data:
    print(doc.page_content)
