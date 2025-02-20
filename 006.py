def join_first_last(input_str):
    # 在此处编写你的代码
    new_str = input_str[0] + input_str[-1]
    return new_str

# 输入字符串
given_string = input()

# 调用函数
print(join_first_last(given_string))