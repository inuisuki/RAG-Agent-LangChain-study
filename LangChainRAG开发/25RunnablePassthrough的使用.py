from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models import ChatTongyi
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.vectorstores import InMemoryVectorStore
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

model=ChatTongyi(model="qwen3-max")
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","以我们提供的资料为主，情简洁回答问题,{context}"),
        ("user","请问该如何减肥{input}")
    ]
)


vector_store = InMemoryVectorStore(
    embedding=DashScopeEmbeddings(model="text-embedding-v4")
)
vector_store.add_texts(["减肥要注意睡眠","减肥要少吃多餐","减肥要少吃多练"])
input_text="请问如何减肥"

def format_func(docs):
    if not docs:
        return "无相关参考资料"

    formatted_str = "["
    for doc in docs:
        formatted_str+=doc.page_content
    formatted_str+="]"

retriever = vector_store.as_retriever(search_kwargs={"k": 2})
chain=(
    {"inpute":RunnablePassthrough(),"context":retriever | format_func} | prompt | model | StrOutputParser()
)
chain.invoke(input_text)
#as_retriever返回一个runnable子类的实例对象
#构建链 retriever ：输入：用户输入（str）；输出：向量库的检索 list【document】
#promt：输入：用户提问+向量数据库的结果dict 输出：完整的提示词promptvalue
print(chain)



