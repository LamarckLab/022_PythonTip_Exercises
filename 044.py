def shift_char(word):
    # 此处编写你的代码 
    ouput_word = ""
    for digit in word:
        digit = chr(ord(digit)+1)
        ouput_word += digit
    return ouput_word

# 获取单词
word = input()
# 调用函数 
print(shift_char(word))
