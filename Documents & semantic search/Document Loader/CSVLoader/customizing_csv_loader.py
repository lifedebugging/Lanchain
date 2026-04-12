from langchain_community.document_loaders.csv_loader import CSVLoader
from pathlib import Path

loader = CSVLoader(
    file_path=r"D:\Downloads\sample-csv-files-sample-6.csv",
    csv_args={
        "delimiter" : ",",
        "fieldnames" : ["First_name", "Last_name"],
    }
)

data = loader.load()


print(data[1].page_content)
print(data[0].metadata)
    
