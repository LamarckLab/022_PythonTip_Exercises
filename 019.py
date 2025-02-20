def ends_with(string1, string2):
    # 此处写你的代码
    flag = string1.endswith(string2)
    return flag

# 获取输入字符串
string1 = input()
string2 = input()
# 调用函数
print(ends_with(string1, string2))