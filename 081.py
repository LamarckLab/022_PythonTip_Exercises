def check_consecutive_sum(n):
    # 此处写代码
    my_sum = 0
    for i in range(1,n):
        my_sum = i
        for j in range(i+1,n):
            my_sum += j
            if my_sum == n:
                return True
            elif my_sum > n:
                my_sum = 0
                break
    return

# 获取输入数字n
n = int(input())

# 调用函数 
print(check_consecutive_sum(n))