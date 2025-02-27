def repeat_till_equal_length(string1, string2):
    # 在此处编写你的代码
    if len(string1) < len(string2):
        short_str = string1
        long_str = string2
    else:
        short_str = string2
        long_str = string1
    mutiple = len(long_str) // len(short_str) + 1
    target_str = short_str * mutiple
    return target_str[:len(long_str)]

# 输入两个字符串
string1 = input()
string2 = input()
# 调用函数
print(repeat_till_equal_length(string1, string2))