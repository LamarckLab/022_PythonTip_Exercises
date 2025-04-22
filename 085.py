def sum_of_digits_in_factorial(num):
    # 在此处编写你的代码
    factorial = 1
    digit_sum = 0
    while num > 0:
        factorial *= num
        num -= 1
    for digit in str(factorial):
        digit_sum += int(digit)
    return digit_sum

# 获取用户输入
num = int(input())

# 调用函数
print(sum_of_digits_in_factorial(num))
