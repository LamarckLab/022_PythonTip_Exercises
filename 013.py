def reverse_number_digits(num):
    # 在此处编写你的代码
    my_list = []
    while num > 0:
        digit = num % 10
        my_list.append(digit)
        num //= 10
    return my_list

# 获取用户输入
num = int(input())

# 调用函数
print(reverse_number_digits(num))