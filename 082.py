def is_heterogram(s):
    # 此处编写代码
    extract_s = s.replace(" ","")
    flag = True
    for element in extract_s:
        if extract_s.count(element) > 1:
            flag = False
    if flag:
        return "Yes"
    else:
        return "No"

# 获取输入 
input_string = input()

# 调用函数，输出结果 
print(is_heterogram(input_string))
