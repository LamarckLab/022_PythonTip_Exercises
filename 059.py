def count_consonants(word):
    # 在此处编写你的代码
    consonants_cnt = 0
    word = word.lower()
    for element in word:
        if element in consonants:
            consonants_cnt += 1
    return consonants_cnt

def count_vowels(word):
    # 在此处编写你的代码
    vowels_cnt = 0
    word = word.lower()
    for element in word:
        if element in vowels:
            vowels_cnt += 1
    return vowels_cnt

# 获取用户输入
word = input()

vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
# 调用函数
print(count_consonants(word))
print(count_vowels(word))