def sum_of_digits_in_factorial(num):
    # 在此处编写你的代码
    factorial = 1
    target_sum = 0
    if num <= 1:
        return 1
    else:
        for i in range(1,num+1):
            factorial *= i
    for element in str(factorial):
        target_sum += int(element)
    return target_sum

# 获取用户输入
num = int(input())

# 调用函数
print(sum_of_digits_in_factorial(num))