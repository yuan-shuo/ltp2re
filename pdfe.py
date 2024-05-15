import PyPDF2

class PdfE:
    def __init__(self):
        self.id = 'pdfe'
    def deal(self, path):
        text = ""
        with open(path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            for page_num in range(num_pages):
                page = reader.pages[page_num]
                text += page.extract_text()
        # 移除换行符
        text = text.replace("\n", "")
        return text
    
if __name__ == '__main__':
    a = PdfE()
    print(a.deal("pdfSQL/topdf.pdf"))
