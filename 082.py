def is_heterogram(s):
    # 此处编写代码
    s = s.replace(" ","")
    target_dict = {}
    for element in s:
        if element not in target_dict:
            target_dict[element] = 1
        else:
            target_dict[element] += 1
    for element in target_dict:
        if target_dict[element] > 1:
            return "No"
    return "Yes"



# 获取输入 
input_string = input()

# 调用函数，输出结果 
print(is_heterogram(input_string))