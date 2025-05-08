def is_email_valid(email):
    # 此处编写代码
    if "@" not in email or "." not in email or email.index("@") == 0 or email[::-1].index(".") != 3:
        return False
    return True

# 获取输入 
email = input()

# 调用函数 
print(is_email_valid(email))
