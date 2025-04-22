def flatten_list(list_of_lists):
    # 在此处编写你的代码
    output_lst = []
    for sub_lst in list_of_lists:
        for letter in sub_lst:
            if letter not in output_lst:
                output_lst.append(letter)
    return sorted(output_lst)
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
