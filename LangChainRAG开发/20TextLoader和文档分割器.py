from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = TextLoader(file_path="./data/Python的基础语法.txt",encoding="utf-8")

docs=loader.load()

spliter=RecursiveCharacterTextSplitter(
    chunk_size=100,  # 分段最大字符树
    chunk_overlap=50,  # 分段之间允许重叠字数
    separators=["/n/n", "/n", "？", "，", "。", "！", "?", ",", ".", "!"],  # 段落分割允许的符号
    length_function=len
)
split_doc=spliter.split_documents(docs)
print(len(split_doc))
for doc in split_doc:
    print("="*20)
    print(doc)
    print("="*20)