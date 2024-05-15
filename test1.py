import torch
from ltp import LTP, StnSplit

# 默认 huggingface 下载，可能需要代理

ltp = LTP(r"E:\python_work\pyneo\pdfToData\myPDF\models\tiny")  # 默认加载 Small 模型
                        # 也可以传入模型的路径，ltp = LTP("/path/to/your/model")
                        # /path/to/your/model 应当存在 config.json 和其他模型文件

# 将模型移动到 GPU 上
if torch.cuda.is_available():
    # ltp.cuda()
    ltp.to("cuda")

# 自定义词表
# ltp.add_word("汤姆去", freq=2)
# ltp.add_words(["隧道围岩分级", "yuan"], freq=2)
sents = StnSplit().split(
    "李克强总理今天来我家了,我感到非常荣幸。钻孔桩造价低于地下连续墙。"
    )
print(sents)
output = ltp.pipeline(sents, tasks=["cws", "pos", "srl"])

print(f"分词：{output.cws}")
print(f"词性：{output.pos}")
print(f"语义角色标注：{output.srl}")

def aa(sent):
    res = []
    for content in sent: # 一句话
        for item in content: # 一句话里的每个小字典
            if any(role_type == 'A0' for role_type, _ in item['arguments']) and any(role_type == 'A1' for role_type, _ in item['arguments']):
                subject_value = None  
                object_value = None  
                for role_type, value in item['arguments']:  
                    if role_type == 'A0':  
                        subject_value = value  
                    elif role_type == 'A1':  
                        object_value = value  
                if subject_value and object_value:  
                    res.append({'subject': subject_value, 'relation': item['predicate'], 'object': object_value})
    return res

print(aa(output.srl))
