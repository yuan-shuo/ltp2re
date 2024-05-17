# pip install -r requirements.txt

from l2neo import l2neo
from te import te
from pdfe import PdfE
import os
from py2neo import Graph

class Maine:
    def __init__(self, wordList=[]) -> None:
        self.te = te(words=wordList)
        self.pdfe = PdfE()
    def run(self, pathe):
        file_name, _ = os.path.splitext(os.path.basename(pathe))
        self.l2neo = l2neo(syz=self.te.deal(self.pdfe.deal(path=pathe)), filename=file_name)
        self.l2neo.go()

if __name__ == '__main__':
    import os
    import shutil

    link = Graph("http://localhost:7474", auth=("neo4j", "174235"))
    graph = link
    query = "MATCH (u:CoreBook) RETURN u.name AS name"
    result = graph.run(query)
    al = [record["name"] for record in result]

    folder_path = r"F:\neoSQL\文献"
    a = Maine()

    unf = []
    target_dir = r'F:\neoSQL\disable'
    for root, dirs, files in os.walk(folder_path):
        
        for file in files:
            file_path = os.path.join(root, file)
            file_name, _ = os.path.splitext(os.path.basename(file_path))
            if file_name in al:
                print("重复文件，跳过")
                continue
            print(f"正在处理：{file_path}")
            try:
                a.run(file_path)
            except:
                unf.append(file_path)
                shutil.move(file_path, target_dir) 
    print(f"未执行：{len(unf)}")
    for i in unf:
        print(i)
        

    # a = Maine()
    # a.run("pdfSQL/大断面砂质板岩隧道围岩动态...析——以道吾山特长隧道为例_袁枫斌.pdf")