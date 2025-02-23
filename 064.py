def common_letters(word1, word2):
    # 此处编写代码
    common_letters_set = set(word1).intersection(set(word2))
    common_letters_lst = sorted(list(common_letters_set))
    target = ""
    for element in common_letters_lst:
        target += element
    return target

# 输入两个单词
word1 = input()
word2 = input()

# 调用函数, 并打印结果
print(common_letters(word1, word2))