def is_sum_even(string):
    # 此处编写你的代码
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    index_sum = 0
    string = string.lower()
    for letter in string:
        if letter in alphabet:
            index_sum += alphabet.index(letter) + 1
    return index_sum % 2 == 0

# 获取字符串 
string = input()

# 调用函数 
print(is_sum_even(string))
