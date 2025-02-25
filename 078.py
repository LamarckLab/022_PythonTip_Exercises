def repetitions_in_string(s):
    # 此处编写代码
    s_len = len(s)
    for subs_len in range(1,s_len):
        if s_len % subs_len == 0:
            if s[:subs_len] * (int(s_len/subs_len)) == s:
                return int(s_len/subs_len)
    return 1

# 获取输入 
test_string = input()

# 调用函数 
print(repetitions_in_string(test_string))