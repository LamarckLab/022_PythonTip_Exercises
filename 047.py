def get_missing_letters(word_string):
    # 此处编写你的代码 
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in word_string:
        alphabet = alphabet.replace(letter,"")
    return alphabet
# 获取输入的字符串 
word_string = input()

# 调用函数输出结果 
print(get_missing_letters(word_string))
