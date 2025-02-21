import datetime

def calculate_days_between(date1, date2):
    # 在此处编写你的代码
    date_format = "%Y-%m-%d" # 日期格式
    d1 = datetime.datetime.strptime(date1, date_format) # 将字符串转换为datetime对象
    d2 = datetime.datetime.strptime(date2, date_format)
    difference = d2 - d1 # 计算两个日期之间的差异
    return difference.days # 以天数的差异作为输出返回
# 获取用户输入
date1 = input()
date2 = input()

# 调用函数
print(calculate_days_between(date1, date2))