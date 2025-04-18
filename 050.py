def count_char_occurrences(sentence, char):
    # 此处编写你的代码
    output_lst = []
    count = 0
    word_lst = sentence.lower().split(" ")
    for element in word_lst:
        for digit in element:
            if digit == char:
                count += 1
        output_lst.append(count)
        count = 0
    return output_lst

 
# 获取输入 
sentence_input = input()
char_input = input()

# 调用函数 
print(count_char_occurrences(sentence_input, char_input))
