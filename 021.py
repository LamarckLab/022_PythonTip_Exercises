def is_string_isogram(word):
    # 将单词转换为小写
    word = word.lower()
    # 在此处编写你的代码
    my_list = []
    for item in word:
        my_list.append(item)
    my_set = set(my_list)
    return len(my_list) == len(my_set)

# 从用户处获取输入
word = input()
# 调用函数
print(is_string_isogram(word))
