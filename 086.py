def largest_prime_factor(num):
    # 此处编写代码
    i = 2
    while i < num:
        if num % i == 0:
            num //= i
        else:
            i += 1 
    return num

# 获取输入数字
user_input = int(input())

# 调用函数 
print(largest_prime_factor(user_input))