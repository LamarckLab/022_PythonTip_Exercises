def closest_vowel(letter):
    # 此处编写代码 
    if letter <= 'c':
        return 'a'
    elif letter <= 'g':
        return 'e'
    elif letter <= 'l':
        return 'i'
    elif letter <= 'r':
        return 'o'
    else:
        return 'u'
# 获取输入
letter = input()
# 调用函数
print(closest_vowel(letter))
