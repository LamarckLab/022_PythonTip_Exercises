def check_prime(num):
    # 在此处编写代码
    flag = True
    for i in range(2, num):
        if num % i == 0:
            flag = False
    return flag
# 输入一个整数
number = int(input())

# 调用函数
print(check_prime(number))