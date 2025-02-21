def smallest_multiple(n):
    # 此处写你的代码
    target = n
    while True:
        if all(target % i == 0 for i in range(1, n+1)):
            return target
        target += 1

# 输入n
n = int(input())
# 调用函数
print(smallest_multiple(n))