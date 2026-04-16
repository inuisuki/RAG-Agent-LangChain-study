from langchain_community.document_loaders import JSONLoader

loader = JSONLoader(
    file_path="",  # json文件位置
    jq_schema="name",  # .是所有文件，[]取数组，对于jasonline可以直接取name
    text_content=False,  # 判断是否为string
    json_lines=False  # 判断是否为jsonline
)
document=loader.load()
print(document)