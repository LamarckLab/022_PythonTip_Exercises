def check_double_base_palindrome(number):
    # 此处编写代码
    str_num = str(number)
    str_bin_num = bin(number)[2:]
    return (str_num == str_num[::-1]) and (str_bin_num == str_bin_num[::-1])

# 获取用户输入
number = int(input())

# 调用函数
print(check_double_base_palindrome(number))
