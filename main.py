from l2neo import l2neo
from te import te
from pdfe import PdfE

class Maine:
    def __init__(self, wordList=[]) -> None:
        self.te = te(words=wordList)
        self.pdfe = PdfE()
    def run(self, pathe):
        self.l2neo = l2neo(self.te.deal(self.pdfe.deal(path=pathe)))
        self.l2neo.go()

if __name__ == '__main__':
    a = Maine()
    a.run("pdfSQL/pdfa1.pdf")