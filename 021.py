def is_string_isogram(word):
    # 将单词转换为小写
    word = word.lower()
    # 在此处编写你的代码
    for element in word:
        if word.count(element) > 1:
            return False
    return True
# 从用户处获取输入
word = input()
# 调用函数
print(is_string_isogram(word))
