def sort_by_last_char(sentence):
     # 此处编写代码
     word_list = sentence.split(" ")
     sorted_list = sorted(word_list, key = lambda x: x[-1])
     return " ".join(sorted_list)
# 输入句子 
sentence = input()

# 调用函数 
print(sort_by_last_char(sentence))
