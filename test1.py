from py2neo import Graph

link = Graph("http://localhost:7474", auth=("neo4j", "174235"))
graph = link

# 查询所有用户节点的名称
query = "MATCH (u:CoreBook) RETURN u.name AS name"
result = graph.run(query)

# 存储名称的列表
name_list = [record["name"] for record in result]

# 打印名称列表
print(name_list)
