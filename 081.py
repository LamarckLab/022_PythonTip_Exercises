def check_consecutive_sum(n):
    # 此处写代码
    sum_temp = 0
    for i in range(1,n):
        sum_temp += i
        for j in range(i+1,n):
            sum_temp += j
            if sum_temp == n:
                return True
            elif sum_temp > n:
                sum_temp = 0
                continue
    return False
# 获取输入数字n
n = int(input())

# 调用函数
print(check_consecutive_sum(n))
