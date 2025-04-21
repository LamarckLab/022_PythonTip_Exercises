def convert_str_list_to_dict(str_list):
    # 此处编写代码
    output_dict = {}
    string_lst = str_list.split(" ")
    for element in string_lst:
        equal_index = element.index("=")
        output_dict[element[:equal_index]] = element[equal_index+1:]
    return output_dict

# 输入字符串 
str_list = input()

# 调用函数 
print(convert_str_list_to_dict(str_list))
