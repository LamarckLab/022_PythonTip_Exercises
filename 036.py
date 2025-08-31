def is_harshad(num):
    # 在此处编写你的代码
    digit_sum, origin_num = 0, num
    while num > 0:
        digit_sum += (num % 10)
        num //= 10
    return origin_num % digit_sum == 0
# 获取用户输入
num = int(input())

# 显示输出
print(is_harshad(num))
