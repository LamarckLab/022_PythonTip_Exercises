def common_letters(word1, word2):
    # 此处编写代码
    return "".join(sorted(set(word1) & set(word2)))
# 输入两个单词
word1 = input()
word2 = input()

# 调用函数, 并打印结果
print(common_letters(word1, word2))
