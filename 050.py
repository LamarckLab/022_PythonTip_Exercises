def count_char_occurrences(sentence, char):
    # 此处编写你的代码
    word_list = sentence.lower().split(" ")
    times_list = []
    for word in word_list:
        times_list.append(word.count(char))
    return times_list
# 获取输入 
sentence_input = input()
char_input = input()

# 调用函数 
print(count_char_occurrences(sentence_input, char_input))
