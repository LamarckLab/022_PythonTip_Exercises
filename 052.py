def get_longest_word(sentence):
    # 在此处编写你的代码
    word_list = sentence.split(" ")
    longest_word = ""
    for word in word_list:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word
# 获取输入 
sentence = input()

# 调用函数 
print(get_longest_word(sentence))
