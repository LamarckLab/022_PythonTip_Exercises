def sort_by_last_char(sentence):
     # 此处编写代码
     words_lst = sentence.split(" ")
     for i in range(len(words_lst)):
          words_lst[i] = words_lst[i][::-1]
     words_lst = sorted(words_lst)
     for i in range(len(words_lst)):
          words_lst[i] = words_lst[i][::-1]
     return " ".join(words_lst)
     
# 输入句子 
sentence = input()

# 调用函数 
print(sort_by_last_char(sentence))
