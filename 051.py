def add_space_before_capital(word):
    # 在此处编写你的代码
    output_sentence = ""
    for letter in word:
        if letter.islower():
            output_sentence += letter
        else:
            output_sentence += (" " + letter.lower())
    return output_sentence
# 获取用户输入
word = input()

# 调用函数
print(add_space_before_capital(word))
