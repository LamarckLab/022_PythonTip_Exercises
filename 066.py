def is_string_palindrome(string):
    # 此处编写代码
    if len(string) < 2:
        return True
    else:
        if string[0] == string[-1]:
            return is_string_palindrome(string[1:-1])
        else:
            return False

# 获取用户输入
user_input = input()

# 调用函数
print(is_string_palindrome(user_input.lower()))
