def is_date_palindromic(date_in_string):
    # 此处编写你的代码
    flag1 = True
    flag2 = True
    str1 = date_in_string[:2] + date_in_string[3:5] + date_in_string[6:10]
    str2 = date_in_string[3:5] + date_in_string[:2] + date_in_string[6:10]
    if str1 != str1[::-1]:
        flag1 = False
    if str2 != str2[::-1]:
        flag2 = False
    return flag1 and flag2

# 获取日期输入 
date_in_string = input()

# 调用函数 
print(is_date_palindromic(date_in_string))