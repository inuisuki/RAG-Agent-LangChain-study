import json
#创建元组
d={
    "name":"周杰伦",
    "age":"24",
    "gender":"男"
}
print(str(d))
#python转json
s=json.dumps(d,ensure_ascii=False)
print(s)

l=[
    {
    "name":"周杰伦",
    "age":"24",
    "gender":"男"
},
 {
    "name":"蔡依林",
    "age":"18",
    "gender":"女"
},
 {
    "name":"方浩",
    "age":"24",
    "gender":"男"
},
]
s=json.dumps(l,ensure_ascii=False)
print(s)

json_str='{"name": "周杰伦", "age": "24", "gender": "男"}'
json_arry_str='[{"name": "周杰伦", "age": "24", "gender": "男"}, {"name": "蔡依林", "age": "18", "gender": "女"}, {"name": "方浩", "age": "24", "gender": "男"}]'

res_dirt=json.loads(json_str)
print(res_dirt,type(res_dirt))
res_list=json.loads(json_arry_str)
print(res_list,type(res_list))