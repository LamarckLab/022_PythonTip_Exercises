def find_gcd(a, b):
    # 在此处编写代码
    my_min = min(a,b)
    gcd = 1
    for i in range(1,my_min+1):
        if (a%i == 0) & (b%i == 0):
            gcd = i
    return gcd
# 输入整数
first_number = int(input())
second_number = int(input())
# 调用函数
print(find_gcd(first_number, second_number))