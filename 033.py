def calculate_sum(numbers_list):
    # 此处编写代码
    odd_sum, even_sum = 0, 0
    for digit in numbers_list:
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
    return [even_sum, odd_sum]
# 获取输入转为列表
numbers_list = list(map(int,input().split()))

# 打印偶数和奇数的和
print(calculate_sum(numbers_list))
