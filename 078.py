def repetitions_in_string(s):
    # 此处编写代码
    sublen = 1
    while sublen <= len(s):
        if s[:sublen] * (len(s)//sublen) == s:
            return len(s)//sublen
        sublen += 1
# 获取输入 
test_string = input()

# 调用函数 
print(repetitions_in_string(test_string))
