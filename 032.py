def find_highest_number(numbers_list):
    # 此处编写代码
    return max(numbers_list)

# 输入数字并转为列表
numbers_list = list(map(int, input().split()))

# 调用函数打印结果
print(find_highest_number(numbers_list))
