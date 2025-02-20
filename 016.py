def is_product_divisible_by_sum(numbers_list):
    # 此处编写代码
    my_product = 1
    my_sum = 0
    for element in numbers_list:
        my_product *= element
        my_sum += element
    if my_product % my_sum == 0:
        return True
    else:
        return False

# 获取整数输入并将其转换为列表
numbers_list = list(map(int, input().split()))
# 调用函数打印结果
print(is_product_divisible_by_sum(numbers_list))