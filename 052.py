def get_longest_word(sentence):
    # 在此处编写你的代码
    target_dict = {}
    max_len = 0
    sentence_list = sentence.split(" ")
    for element in sentence_list:
        target_dict[element] = len(element)
        if len(element) > max_len:
            max_len = len(element)
    for element in target_dict:
        if target_dict[element] == max_len:
            return element

# 获取输入 
sentence = input()

# 调用函数 
print(get_longest_word(sentence))