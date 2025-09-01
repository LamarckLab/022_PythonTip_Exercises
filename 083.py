def is_subset(sub_string, main_string):
    # 在此处编写你的代码
    sub_list, main_list = list(sub_string), list(main_string)
    for letter in sub_string:
        if letter in main_string:
            sub_list.remove(letter)
    return len(sub_list) == 0
# 获取用户输入
sub_string = input()
main_string = input()

# 调用函数
print(is_subset(sub_string, main_string))
