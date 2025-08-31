def find_unique(lst):
    # 此处编写代码
    unique_list = []
    for digit in lst:
        if lst.count(digit) == 1:
            unique_list.append(digit)
    return unique_list
# 获取用户输入并转为数字列表
numbers = list(map(int, input().split()))

# 调用函数
print(find_unique(numbers))
