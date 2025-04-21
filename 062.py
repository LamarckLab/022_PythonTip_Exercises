def is_date_palindromic(date_in_string):
    # 此处编写你的代码
    date_ddmmyyyy = date_in_string[:2] + date_in_string[3:5] + date_in_string[6:]
    date_mmddyyyy = date_in_string[3:5] + date_in_string[:2] + date_in_string[6:]
    return date_ddmmyyyy == date_ddmmyyyy[::-1] and date_mmddyyyy == date_mmddyyyy[::-1]

# 获取日期输入 
date_in_string = input()

# 调用函数 
print(is_date_palindromic(date_in_string))
