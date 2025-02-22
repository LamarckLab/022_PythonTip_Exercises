def is_sum_even(string):
    # 此处编写你的代码
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    index_sum = 0
    for element in string:
        if element in alphabet:
            index_sum += alphabet.index(element) + 1
    if index_sum % 2 == 0:
        return True
    else:
        return False
# 获取字符串 
string = input()

# 调用函数 
print(is_sum_even(string))s