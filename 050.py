def count_char_occurrences(sentence, char):
    # 此处编写你的代码
    sentence = sentence.lower()
    word_list = sentence.split(" ")
    cnt_list = []
    cnt = 0
    for element in word_list:
        for digit in element:
            if digit == char:
                cnt += 1
        cnt_list.append(cnt)
        cnt = 0
    return cnt_list
 
# 获取输入 
sentence_input = input()
char_input = input()

# 调用函数 
print(count_char_occurrences(sentence_input, char_input))