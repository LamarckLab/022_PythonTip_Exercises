def get_unique_elements(nested_tuples):
    # 此处编写代码
    my_list = []
    for i in range(3):
        for j in range(len(nested_tuples[i])):
            my_list.append(nested_tuples[i][j])
    my_list = sorted(list(set(my_list)))
    return my_list
# 初始化嵌套元组
nested_tuples = []

# 获取用户输入
for _ in range(3):
    tuple_elements = tuple(map(int, input().split()))
    nested_tuples.append(tuple_elements)

# 调用函数
print(get_unique_elements(nested_tuples))