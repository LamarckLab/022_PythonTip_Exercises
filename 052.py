def get_longest_word(sentence):
    # 在此处编写你的代码
    sentence_lst = sentence.split(" ")
    max_len = 0
    longest_word = ""
    for word in sentence_lst:
        if len(word) > max_len:
            max_len = len(word)
            longest_word = word
    return longest_word


# 获取输入 
sentence = input()

# 调用函数 
print(get_longest_word(sentence))
