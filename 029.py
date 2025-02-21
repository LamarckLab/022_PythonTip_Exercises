def count_syllables(word):
    # 此处写你的代码 
    cnt = word.count("-") + 1
    return cnt
# 获取用户输入
word = input()
# 调用函数
print(count_syllables(word))