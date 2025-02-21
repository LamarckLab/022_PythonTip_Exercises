def is_title(sentence):
    # 在此处编写代码
    sentence_list =sentence.split()
    flag = True
    for word in sentence_list:
        if not word[0].isupper():
            flag = False
    return flag
# 从用户处获取输入
input_sentence = input()
# 调用函数
print(is_title(input_sentence))