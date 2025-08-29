def check_prime(num):
    # 在此处编写代码
    if num == 2:
        return False
    else:
        for i in range(2,num):
            if num % i == 0:
                return False
        return True
# 输入一个整数
number = int(input())

# 调用函数
print(check_prime(number))
