def shift_char(word):
    # 此处编写你的代码
    new_word = ""
    for element in word:
        element = chr(ord(element) + 1)
        new_word += element
    return new_word

# 获取单词
word = input()
# 调用函数 
print(shift_char(word))