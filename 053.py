def check_perfect(num):
    # 此处编写你的代码
    factor_sum = 0
    for i in range(1,num):
        if num % i == 0:
            factor_sum += i
    return factor_sum == num
# 输入处理 
num = int(input())

# 调用函数 
print(check_perfect(num))
