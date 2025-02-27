def extreme_words_in_sentence(sentence):
    # 此处编写你的代码
    sentence = sentence.lower()
    sentence_list = sentence.split(" ")
    long_word = ''
    short_word = 'lamarck nb'
    for element in sentence_list:
        if len(element) > len(long_word):
            long_word = element
        if len(element) < len(short_word):
            short_word = element
    return (long_word,short_word)

# 处获取输入
sentence = input()
# 调用函数
print(extreme_words_in_sentence(sentence))