def count_consonants(word):
    # 在此处编写你的代码
    consonants_str ="bcdfghjklmnpqrstvwxyz"
    consonants_count = 0
    for letter in word.lower():
        if letter in consonants_str:
            consonants_count += 1
    return consonants_count

def count_vowels(word):
    # 在此处编写你的代码
    vowels_str = "aeiou"
    vowels_count = 0
    for letter in word.lower():
        if letter in vowels_str:
            vowels_count += 1
    return vowels_count

# 获取用户输入
word = input()

# 调用函数
print(count_consonants(word))
print(count_vowels(word))
