tem = {'arguments': [('A0', '李克强总理'), ('ARGM-TMP', '今天'), ('A1', '我家')]}  
  
# 检查 'arguments' 是否同时包含 'A0' 和 'A1'  
contains_a0_and_a1 = all(role_type in ('A0', 'A1') for role_type, _ in tem['arguments'])  
  
# 但上面的代码会错误地认为只要 'A0' 或 'A1' 中的一个出现就满足条件  
# 因此，我们需要分别检查它们是否存在  
contains_a0 = any(role_type == 'A0' for role_type, _ in tem['arguments'])  
contains_a1 = any(role_type == 'A1' for role_type, _ in tem['arguments'])  
  
# 最终判断  
if contains_a0 and contains_a1:  
    print("tem['arguments'] 同时包含 A0 和 A1")  
else:  
    print("tem['arguments'] 不同时包含 A0 和 A1")