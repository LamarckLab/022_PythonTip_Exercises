def flatten_list(list_of_lists):
    # 在此处编写你的代码
    output_list = []
    for sublist in list_of_lists:
        for digit in sublist:
            if digit not in output_list:
                output_list.append(digit)
    return sorted(output_list)
# 初始化嵌套列表
list_of_lists = []

# 获取用户输入
# 子列表的数量
n = int(input())

# 子列表
for _ in range(n):
    sublist = list(map(int, input().split()))
    list_of_lists.append(sublist)

# 调用函数
print(flatten_list(list_of_lists))
