def get_unique_elements(nested_tuples):
    # 此处编写代码
    output_lst =[]
    for sub_tuple in nested_tuples:
        for item in sub_tuple:
            if item not in output_lst:
                output_lst.append(item)
    return sorted(output_lst)

# 初始化嵌套元组
nested_tuples = []

# 获取用户输入
for _ in range(3):
    tuple_elements = tuple(map(int, input().split()))
    nested_tuples.append(tuple_elements)

# 调用函数
print(get_unique_elements(nested_tuples))
