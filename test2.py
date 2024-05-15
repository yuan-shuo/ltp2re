a = [[{'predicate': '来', 'arguments': [('A0', '李克强总理'), ('ARGM-TMP', '今天'), ('A1', '我家')]}, 
      {'predicate': '感到', 'arguments': [('A0', '我'), ('A1', '非常荣幸')]}, 
      {'predicate': '荣幸', 'arguments': [('ARGM-ADV', '非常')]}],
        [{'predicate': '低于', 'arguments': [('A0', '钻孔桩造价'), ('A1', '地下连续墙')]}]]

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

print(aa(a))