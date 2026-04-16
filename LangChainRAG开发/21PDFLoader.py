from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(
    file_path="./data/sample-local-pdf.pdf"
)
i=0
for page in loader.lazy_load():
    i+=1
    print(page,i)