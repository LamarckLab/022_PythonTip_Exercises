def is_harshad(num):
    # 在此处编写你的代码
    digit_sum = 0
    flag = False
    temp = num
    while temp >= 1:
        digit_sum += (temp%10)
        temp //= 10
    if num % digit_sum == 0:
        flag = True
    return flag

# 获取用户输入
num = int(input())

# 显示输出
print(is_harshad(num))