def get_missing_letters(word_string):
    # 此处编写你的代码
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    target_str = ""
    for element in alphabet:
        if element not in word_string:
            target_str += element
    return target_str

# 获取输入的字符串 
word_string = input()

# 调用函数输出结果 
print(get_missing_letters(word_string))