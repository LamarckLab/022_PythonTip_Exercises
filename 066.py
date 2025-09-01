def is_string_palindrome(string):
    # 此处编写代码
    if len(string) < 2 or string == string[::-1]:
        return True
    else:
        return False
# 获取用户输入
user_input = input()

# 调用函数
print(is_string_palindrome(user_input.lower()))
