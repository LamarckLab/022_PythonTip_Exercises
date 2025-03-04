def split_string_into_clusters(input_str):
    # 此处编写代码
    target_lst = []
    temp_substr = ""
    for index in range(0,len(input_str)-1):
        if temp_substr == "":
            temp_substr += input_str[index]
        if input_str[index+1] == input_str[index]:
            temp_substr += input_str[index+1]
        else:
            target_lst += [temp_substr]
            temp_substr = ""
            if index == len(input_str) - 2:
                target_lst += [input_str[-1]]
    return target_lst

# 获取用户输入
input_string = input()
# 调用函数，输出结果
print(split_string_into_clusters(input_string)) 