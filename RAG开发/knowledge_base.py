import os
import hashlib
import config_data as config
from datetime import datetime
from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

def check_md5(md5_str: str) -> bool:
    if not os.path.exists(config.md5_path):
        open(config.md5_path,"w",encoding="utf-8").close()
        return False
    else:
        for line in open(config.md5_path,"r",encoding="utf-8").readlines():
            line = line.strip()#去掉回车和空格
            if(line == md5_str):
                return True
        return False


def save_md5(md5_str: str):
    with open(config.md5_path,"a",encoding="utf-8") as f:
        f.write(md5_str+'\n')


def get_string_md5(input_str:str,encoding='utf-8'):
    str_bytes = input_str.encode(encoding=encoding)
    md5_obj = hashlib.md5()#得到md5对象
    md5_obj.update(str_bytes)#更新内容（传入将要转换的字节数组）
    md5_hex=md5_obj.hexdigest()
    return md5_hex

class KnowledgeBaseService(object):
    os.makedirs(config.persist_directory,exist_ok=True)
    def __init__(self):
        self.chroma=Chroma(
            collection_name=config.collections_name,#数据库表名
            embedding_function=DashScopeEmbeddings(model="text-embedding-v4"),
            persist_directory=config.persist_directory
        )
        self.spliter=RecursiveCharacterTextSplitter(
            chunk_size=config.chunk_size,
            chunk_overlap=config.chunk_overlap,
            separators=config.separators,
            length_function=len
        )


    def upload_by_str(self,data,filename):
        md5_hex=get_string_md5(data)
        if(check_md5(md5_hex)):
            return "[跳过]内容已在知识库里"

        if(len(data)>config.max_split_char_number):
            knowledge_chunks=self.spliter.split_text(data)
        else:
            knowledge_chunks=[data]

        metadata={
            "source": filename,
            "creat_time":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "operator":"小刘"
        }

        self.chroma.add_texts(
            knowledge_chunks,
            metadata=[metadata for _ in knowledge_chunks]
        )
        save_md5(md5_hex)
        return "[成功]内容已成功记录"

if __name__ == '__main__':
    service=KnowledgeBaseService()
    r=service.upload_by_str("周杰伦","testfile")
    print(r)