def repetitions_in_string(s):
    # 此处编写代码
    for sub_len in range(1,len(s)+1):
        if len(s) % sub_len == 0:
            if s[:sub_len] * (int(len(s)/sub_len)) == s:
                return int(len(s)/sub_len)

# 获取输入 
test_string = input()

# 调用函数 
print(repetitions_in_string(test_string))
