def shift_char(word):
    # 此处编写你的代码
    output_word = ""
    for letter in word:
        output_word += chr(ord(letter)+1)
    return output_word
# 获取单词
word = input()
# 调用函数 
print(shift_char(word))
