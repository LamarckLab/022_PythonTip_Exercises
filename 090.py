def is_email_valid(email):
    # 此处编写代码
    flag = True
    if "@" not in email or "." not in email:
        flag = False
    if email.index("@") == 0:
        flag = False
    reverse_email = email[::-1]
    if reverse_email.index(".") != 3:
        flag = False
    return flag

# 获取输入 
email = input()

# 调用函数 
print(is_email_valid(email))