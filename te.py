import torch
from ltp import LTP, StnSplit

class te:
    def __init__(self, words=[]) -> None:
        self.ltp = LTP(r"E:\python_work\pyneo\pdfToData\myPDF\models\tiny")
        if torch.cuda.is_available():
            self.ltp.to("cuda")
        self.ltp.add_words(words, freq=2)
    def deal(self, sent):
        sents = StnSplit().split(sent)
        output = self.ltp.pipeline(sents, tasks=["cws", "srl"])
        return s2tri(output.srl)

def s2tri(sent):
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

if __name__ == '__main__':
    a = te()
    print(a.deal("李克强总理今天来我家了,我感到非常荣幸。钻孔桩造价低于地下连续墙。"))
