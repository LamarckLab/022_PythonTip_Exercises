def reverse_sentence_words(sentence):
    # 此处写你的代码
    my_list = sentence.split(" ")[::-1]
    return " ".join(my_list)
# 获取输入
sentence = input()
# 调用函数并打印结果
print(reverse_sentence_words(sentence))
