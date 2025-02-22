def capitalize_last_letter(sentence):
    # 此处编写你的代码
    digit = ""
    sentence = sentence + " "
    for index in range(0,len(sentence)):
        if sentence[index] == " ":
            digit = sentence[index-1].upper()
            sentence = sentence[:index-1] + digit + sentence[index:]
    return sentence

# 获取输入 
sentence = input()

# 调用函数 
print(capitalize_last_letter(sentence))