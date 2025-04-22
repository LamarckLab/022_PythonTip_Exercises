def check_consecutive_sum(n):
    # 此处写代码
    for i in range(1, n):
        sum = i
        for j in range(i+1, n):
            sum += j
            if sum > n:
                break
            elif sum < n:
                continue
            else:
                return True
    return False


# 获取输入数字n
n = int(input())

# 调用函数 
print(check_consecutive_sum(n))
