def check_duplicate_letters(phrase):
    # 此处编写代码 
    words_list = phrase.split(" ")
    flag = False
    for element in words_list:
        if len(element) != len(set(element)):
            flag = True
    return flag
# 获取输入
sentence = input()
# 调用函数
print(check_duplicate_letters(sentence))