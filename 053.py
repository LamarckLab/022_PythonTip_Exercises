def check_perfect(num):
    # 此处编写你的代码
    divisor_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisor_sum += i
    if num == divisor_sum:
        return True
    else:
        return False
# 输入处理 
num = int(input())

# 调用函数 
print(check_perfect(num))