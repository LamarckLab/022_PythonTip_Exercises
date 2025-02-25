def convert_str_list_to_dict(str_list):
    # 此处编写代码
    target_dict = {}
    my_lst = str_list.split(" ")
    for element in my_lst:
        index = element.index("=")
        target_dict[element[:index]] = element[index+1:]
    return target_dict

# 输入字符串 
str_list = input()

# 调用函数 
print(convert_str_list_to_dict(str_list))