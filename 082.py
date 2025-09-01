def is_heterogram(s):
    # 此处编写代码
    s = s.replace(" ","")
    if sorted(set(s)) == sorted(s):
        return "Yes"
    return "No"
# 获取输入 
input_string = input()

# 调用函数，输出结果 
print(is_heterogram(input_string))
