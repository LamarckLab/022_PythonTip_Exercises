def smallest_multiple(n):
    # 此处写你的代码
    target_num = n*(n-1)
    while True:
        if all(target_num % i == 0 for i in range(1,n+1)):
            return target_num
        else:
            target_num += 1
# 输入n 
n = int(input())
# 调用函数
print(smallest_multiple(n))
