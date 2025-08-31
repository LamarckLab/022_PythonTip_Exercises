def find_indices(my_list, element):
    # 此处编写代码
    index_list = []
    for index in range(len(my_list)):
        if element == my_list[index]:
            index_list.append(index)
    return index_list
# split()函数将输入的字符串分割成一个列表
user_input = input().split()
element = input()

# 调用函数 
print(find_indices(user_input, element))
