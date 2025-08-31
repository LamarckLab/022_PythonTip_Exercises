def check_double_base_palindrome(number):
    # 此处编写代码
    bin_num = bin(number)[2:]
    return (str(number) == str(number)[::-1]) and (bin_num == bin_num[::-1])
# 获取用户输入
number = int(input())

# 调用函数
print(check_double_base_palindrome(number))
