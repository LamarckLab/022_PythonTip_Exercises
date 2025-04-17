def is_title(sentence):
    # 在此处编写代码
    my_list = sentence.split(" ")
    flag = True
    for element in my_list:
        if element[0].islower():
            flag = False
    return flag

# 从用户处获取输入
input_sentence = input()
# 调用函数
print(is_title(input_sentence))
