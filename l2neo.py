from py2neo import Node, Graph, Relationship
import torch
from ltp import LTP

class l2neo:
    def __init__(self, syz, filename, delWarn="n", debug=False):
        self.syz = syz
        self.debug = debug
        self.name = filename
        self.warn = delWarn

    # 启动！
    def go(self):
        if self.debug:
            print("目前以debug模式运行ing，仅打印")
        else:
            # 连接数据库并清空所有内容（要先启动数据库不然先注释掉）
            link = Graph("http://localhost:7474", auth=("neo4j", "174235"))
            self.graph = link

            # # 查询所有用户节点的名称
            # query = "MATCH (u:CoreBook) RETURN u.name AS name"
            # result = self.graph.run(query)
            # if self.name in  [record["name"] for record in result]:
            #     print("重复内容，跳过")
            #     return

            # 实体抽取+去重
            self.list_ner = ner_extract(self.syz)
            # 实体分类
            self.list_type = ner_divide(self.list_ner)

            # warn = input('(__!慎重!__)是否删除原有数据库?(y/n)：')
            warn = self.warn

            if warn == 'y':
                # 删库！慎用
                self.graph.delete_all()
                print("已清空原有数据")
            else:
                print("将保留原有数据库")

            # 绘制节点
            self.plot_point()
            # 绘制联系
            self.plot_relation()

            print("构建任务完成！")
            torch.cuda.empty_cache()
            print("显存释放完成！")
            

    # 画点
    def plot_point(self):
        self.core = Node("CoreBook", name=self.name)
        self.graph.create(self.core)
        for i in range(len(self.list_ner)):
            node = Node(self.list_type[i], name=self.list_ner[i])
            # 绘制代码，debug时注释掉就行
            self.graph.create(node)
            # 链接主节点
            rel = Relationship(node, "content", self.core)
            self.graph.create(rel)

        print("节点绘制完成！")

    # 联系
    def plot_relation(self):
        for item in self.syz:
            subject = self.graph.nodes.match(name=item['subject']).first()
            object = self.graph.nodes.match(name=item['object']).first()
            rel = Relationship(subject, item['relation'], object)
            self.graph.create(rel)
        
        print("联系绘制完成！")

# 提取三元组实体 - 2个（sub+obj）
def ner_extract(list_syz):
    all_ner = []
    for item in list_syz:
        all_ner.append(item['subject'])
        all_ner.append(item['object'])
    # 用set去重省得占用LTP资源
    return list(set(all_ner))

# 实体类别提取 - LTP .GPU
def ner_divide(list_ner):
    all_ner_type = []
    ltp = LTP(r"E:\python_work\pyneo\pdfToData\myPDF\models\tiny")
    if torch.cuda.is_available():
        # ltp.cuda()
        ltp.to("cuda")
    for text in list_ner:
        output = ltp.pipeline([text], tasks=["pos"])
        ner_type = output.pos[0]
        # print(f"{text}的实体类别：{ner_type}")
        all_ner_type.append(ner_type)
    return all_ner_type

if __name__ == '__main__':
    list_syz = [
        {'subject': 'Barack Obama', 'relation': 'was born in', 'object': 'Hawaii'},
        {'subject': 'Richard Manning', 'relation': 'wrote', 'object': 'sentence'},
        ]
    a = l2neo(list_syz, "pdfSQL/pdfa1.pdf")
    a.go()

