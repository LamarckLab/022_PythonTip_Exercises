def is_product_divisible_by_sum(numbers_list):
    # 此处编写代码
    list_product, list_sum = 1, 0
    for element in numbers_list:
        list_product *= element
        list_sum += element
    return list_product % list_sum == 0
# 获取整数输入并将其转换为列表
numbers_list = list(map(int, input().split()))
# 调用函数打印结果
print(is_product_divisible_by_sum(numbers_list))
