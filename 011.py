def vowel_count(string):
    # 此处写你的代码
    cnt = 0 
    for element in string:
        if element in ["a","e","i","o","u"]:
            cnt += 1
    return cnt 

# 获取输入字符串 
input_string = input()
# 调用函数 
print(vowel_count(input_string))