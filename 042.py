def get_unique_elements(nested_tuples):
    # 此处编写代码
    unique_list = []
    for i in range(3):
        for digit in nested_tuples[i]:
            if digit not in unique_list:
                unique_list.append(digit)
    return sorted(unique_list)
# 初始化嵌套元组
nested_tuples = []

# 获取用户输入
for _ in range(3):
    tuple_elements = tuple(map(int, input().split()))
    nested_tuples.append(tuple_elements)

# 调用函数
print(get_unique_elements(nested_tuples))
