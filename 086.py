def largest_prime_factor(num):
    # 此处编写代码
    factor = 2
    while factor < num:
        if num % factor == 0:
            num /= factor
            num = int(num)
        else:
            factor += 1
    return num
    
# 获取输入数字
user_input = int(input())

# 调用函数 
print(largest_prime_factor(user_input))
