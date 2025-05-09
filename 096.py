def extreme_words_in_sentence(sentence):
    # 此处编写你的代码
    word_list = sentence.lower().split(" ")
    longest_word = word_list[0]
    shortest_word = word_list[0]
    for word in word_list:
        if len(word) > len(longest_word):
            longest_word = word
        if len(word) < len(shortest_word):
            shortest_word = word
    return (longest_word, shortest_word)

# 处获取输入
sentence = input()
# 调用函数
print(extreme_words_in_sentence(sentence))
