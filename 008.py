def find_unique_number(num_list):
    # 此处编写你的代码 
    for element in num_list:
        if num_list.count(element) == 1:
            return element
    return None

# 将输入的整数转换为列表
numbers = list(map(int, input().split()))

# 调用函数
print(find_unique_number(numbers))