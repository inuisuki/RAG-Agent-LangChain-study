from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

model=ChatTongyi(model="qwen3-max")
prompt=ChatPromptTemplate.from_template(
    "你需要根据用户会话的历史来回答问题，对话历史：{chat_history}。用户提问：{input}，请回应"
)
str_parser=StrOutputParser()

base_chain=prompt | model | str_parser

story={}

def get_history(session_id):
        if session_id not in story:
            story[session_id]=InMemoryChatMessageHistory()
        return story[session_id]


conversation_chain=RunnableWithMessageHistory(
    base_chain,
    get_history,
    input_messages_key="input",
    history_messages_key="chat_history"
)

if __name__ == '__main__':
    session_config={
        "configurable":{
            "session_id":"user_001"
        }
    }
    res1=conversation_chain.invoke({"input":"之前小明有两个猫"},session_config)
    print("第一次问问题",res1)
    res2=conversation_chain.invoke({"input":"后来小明又养了两只猫"},session_config)
    print("第二次问问题",res2)
    res3=conversation_chain.invoke({"input":"综上所属，小明总共有几只猫"},session_config)
    print("第三次问问题",res3)