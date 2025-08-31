def is_sum_even(string):
    # 此处编写你的代码 
    alphabet = "_abcdefghijklmnopqrstuvwxyz"
    index_sum = 0
    for letter in string.replace(" ","").lower():
        index_sum += alphabet.index(letter)
    return index_sum % 2 == 0
# 获取字符串 
string = input()

# 调用函数 
print(is_sum_even(string))
