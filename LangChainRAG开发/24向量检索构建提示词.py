from langchain_community.chat_models import ChatTongyi
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


model = ChatTongyi(model="qwen3-max")
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","以我提供的参考资料为主，简洁回答问题，参考资料：{context}。"),
        ("user","用户提问：{input}")
    ]
)

vector_store = InMemoryVectorStore(
    embedding=DashScopeEmbeddings(model="text-embedding-v4")
)
vector_store.add_texts(["减肥要注意睡眠","减肥要少吃多餐","减肥要少吃多练"])
input_text="怎么减肥"

result=vector_store.similarity_search(input_text,k=2)

#参考资料构成
reference_text="["
for doc in result:
    reference_text+=doc.page_content
reference_text+="]"
def print_promt(promt):
    print(promt.to_string())
    print("="*20)
    return promt

str_parser=StrOutputParser()

chain=prompt | print_promt | model | str_parser

res=chain.invoke({"input":input_text,"context":reference_text})
print(res)