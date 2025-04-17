def is_harshad(num):
    # 在此处编写你的代码
    digit_sum = 0
    num_copy = num
    while num > 0:
        digit = num % 10
        digit_sum += digit
        num //= 10
    return num_copy % digit_sum == 0

# 获取用户输入
num = int(input())

# 显示输出
print(is_harshad(num))
