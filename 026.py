def fibonacci_number(n):
    # 在此处编写你的代码
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_number(n-1) + fibonacci_number(n-2)

# 输入n的整数
n = int(input())
# 调用函数
print(fibonacci_number(n))
