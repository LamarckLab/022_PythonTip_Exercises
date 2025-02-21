def calculate_sum(numbers_list):
    # 此处编写代码
    even_sum = 0
    odd_sum = 0
    for element in numbers_list:
        if element % 2 == 0:
            even_sum += element
        else:
            odd_sum += element
    return [even_sum,odd_sum]

# 获取输入转为列表
numbers_list = list(map(int,input().split()))

# 打印偶数和奇数的和
print(calculate_sum(numbers_list))