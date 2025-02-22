def count_duplicate_chars(input_string):
    # 在此处编写你的代码
    target_dict = {}
    dup_cnt = 0
    for element in input_string:
        if element not in target_dict:
            target_dict[element] = 1
        else:
            target_dict[element] += 1
    for element in target_dict:
        if target_dict[element] > 1:
            dup_cnt += 1
    return dup_cnt

# 获取用户输入
test_string = input()

# 调用函数
result = count_duplicate_chars(test_string)
print(result)