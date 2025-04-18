def capitalize_last_letter(sentence):
    # 此处编写你的代码
    words_lst = sentence.split(" ")
    new_words_lst = []
    for word in words_lst:
        new_word = word[:-1] + word[-1].upper()
        new_words_lst.append(new_word)
    return " ".join(new_words_lst)

# 获取输入 
sentence = input()

# 调用函数 
print(capitalize_last_letter(sentence))
