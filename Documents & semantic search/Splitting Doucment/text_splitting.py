#text-splitting
from langchain_text_splitters import RecursiveCharacterTextSplitter

#Load example document
with open(r"D:\Downloads\sample_text.txt", encoding='utf-8') as f:
    long_document = f.read()
    print(f"Original text length : {len(long_document)} characters\n")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap = 30,
)

text = text_splitter.create_documents([long_document])
print(f" Splitted into {len(text)} chunks\n")
print('-' * 80)

# To view each chunk
for i, doc in enumerate(text):
    print(f"\n Chunk {i+1}/{len(text)}")
    print('-'*80)
    print(doc.page_content)
    print(f"\n Length : {len(doc.page_content)} characters")

# final observation
print("\n Final observation:")
print(f" - orignal : {len(long_document)} characters")
print(f" -chunks : {len(text)}")
print(f" -average chunk size : {round(len(long_document)/len(text))} characters")
