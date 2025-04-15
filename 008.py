def find_unique_number(num_list):
    # 此处编写你的代码
    for item in num_list:
        if num_list.count(item) == 1:
            return item

# 将输入的整数转换为列表
numbers = list(map(int, input().split()))

# 调用函数
print(find_unique_number(numbers))


###############################################


def find_unique_number(num_list):
    # 此处编写你的代码
    my_dict = {}
    for item in num_list:
        if item not in my_dict:
            my_dict[item] = 1
        else:
            my_dict[item] += 1
    for item in my_dict:
        if my_dict[item] == 1:
            return item

# 将输入的整数转换为列表
numbers = list(map(int, input().split()))

# 调用函数
print(find_unique_number(numbers))
