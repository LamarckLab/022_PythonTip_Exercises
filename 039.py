def check_double_base_palindrome(number):
    # 此处编写代码
    flag_10 = False
    flag_2 = False
    if str(number) == str(number)[::-1]:
        flag_10 = True
    if bin(number)[2:] == (bin(number)[2:])[::-1]:
        flag_2 = True
    return flag_10 and flag_2

# 获取用户输入
number = int(input())

# 调用函数
print(check_double_base_palindrome(number))