import os

folder_path = r"F:\neoSQL\文献"

for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        print(file_path)
