def sort_by_last_char(sentence):
     # 此处编写代码
     sentence_list = sentence.split(" ")
     for index in range(len(sentence_list)):
        sentence_list[index] = sentence_list[index][::-1]
     sentence_list = sorted(sentence_list)
     for index in range(len(sentence_list)):
        sentence_list[index] = sentence_list[index][::-1]
     target = ""
     for element in sentence_list:
        target += (element+" ")
     return target[:-1]

# 输入句子 
sentence = input()

# 调用函数 
print(sort_by_last_char(sentence))