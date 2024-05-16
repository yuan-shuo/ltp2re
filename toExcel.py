from openpyxl import Workbook
from te import te
from pdfe import PdfE
import os

pdfe = PdfE()
tee = te()

folder_path = 'excelSQL'

# 获取excelSQL文件夹下的文件名列表
existing_files = [os.path.splitext(file)[0] for file in os.listdir(folder_path)]

def ee(data, name):
    workbook = Workbook()
    sheet = workbook.active

    # 将新的数据追加到表格中
    for item in data:
        sheet.append([item['subject'], item['relation'], item['object']])

    # 保存Excel文件
    workbook.save('excelSQL/' + name + '.xlsx')

# folder_path = r"F:\neoSQL\文献"
folder_path = r"E:\python_work\pyneo\pdfToData\myPDF\test2\pdfSQL"

for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        file_name, _ = os.path.splitext(os.path.basename(file_path))
        if file_name in existing_files:
            print("重复文件，跳过")
            continue
        print(f"正在处理：{file_path}")
        # print(tee.deal(pdfe.deal(file_path)))
        ee(tee.deal(pdfe.deal(file_path)), name=file_name)


