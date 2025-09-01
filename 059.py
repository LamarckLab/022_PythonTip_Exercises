def count_consonants(word):
    # 在此处编写你的代码
    consonants_cnt = 0
    for letter in word.lower():
        if letter in consonants:
            consonants_cnt += 1
    return consonants_cnt

def count_vowels(word):
    # 在此处编写你的代码
    vowels_cnt = 0
    for letter in word.lower():
        if letter in vowels:
            vowels_cnt += 1
    return vowels_cnt

# 获取用户输入
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
word = input()

# 调用函数
print(count_consonants(word))
print(count_vowels(word))
