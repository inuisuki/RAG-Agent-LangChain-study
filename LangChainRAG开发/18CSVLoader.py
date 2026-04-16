from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path="./data/stu.csv",
    csv_args={
        "delimiter": "，",
        "quotechar": "|",
        "fieldnames": ["name", "gender", "age"],
    },
    encoding="utf-8"
)

##ocuments = loader.load()
#for document in documents:
#   print(document)

for document in loader.lazy_load():
    print(document)
