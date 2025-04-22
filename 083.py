def is_subset(sub_string, main_string):
    # 在此处编写你的代码
    flag = True
    for letter in sub_string:
        if letter not in main_string:
            flag = False
    return flag

# 获取用户输入
sub_string = input()
main_string = input()

# 调用函数
print(is_subset(sub_string, main_string))
