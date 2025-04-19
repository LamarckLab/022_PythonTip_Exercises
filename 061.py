def find_common_elements(list1, list2):
    # 此处编写代码
    output_lst = []
    for element in list1:
        if element in list2:
            output_lst.append(element)
    return sorted(output_lst)

# 获取用户输入，转换为列表
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

# 调用函数
print(find_common_elements(list1, list2))
