def count_duplicate_chars(input_string):
    # 在此处编写你的代码
    duplicate_cnt = 0
    for letter in set(input_string):
        if input_string.count(letter) > 1:
            duplicate_cnt += 1
    return duplicate_cnt
# 获取用户输入
test_string = input()

# 调用函数
result = count_duplicate_chars(test_string)
print(result)
