def add_space_before_capital(word):
    # 在此处编写你的代码
    ouput_word = ""
    for letter in word:
        if letter.islower():
            ouput_word += letter
        else:
            ouput_word += (" " + letter.lower())
    return ouput_word

# 获取用户输入
word = input()

# 调用函数
print(add_space_before_capital(word))
