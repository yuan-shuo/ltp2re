# pip install -r requirements.txt

from l2neo import l2neo
from te import te
from pdfe import PdfE
import os

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

    folder_path = r"F:\neoSQL\文献"
    a = Maine()

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            print(f"正在处理：{file_path}")
            a.run(file_path)

    # a = Maine()
    # a.run("pdfSQL/大断面砂质板岩隧道围岩动态...析——以道吾山特长隧道为例_袁枫斌.pdf")