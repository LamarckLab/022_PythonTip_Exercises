def capitalize_last_letter(sentence):
    # 此处编写你的代码
    word_list = sentence.split(" ")
    upper_list = []
    for word in word_list:
        new_word = word[:-1] + word[-1].upper()
        upper_list.append(new_word)
    return " ".join(upper_list)
# 获取输入 
sentence = input()

# 调用函数 
print(capitalize_last_letter(sentence))
