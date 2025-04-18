def count_duplicate_chars(input_string):
    # 在此处编写你的代码
    my_dict = {}
    count = 0
    for element in input_string:
        if element not in my_dict:
            my_dict[element] = 1
        else:
            my_dict[element] += 1
    for element in my_dict:
        if my_dict[element] != 1:
            count += 1
    return count


# 获取用户输入
test_string = input()

# 调用函数
result = count_duplicate_chars(test_string)
print(result)
