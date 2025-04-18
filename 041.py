def shared_chars_count(word1, word2):
    # 此处编写代码
    return len(set(word1) & set(word2))

# 获取输入
word1 = input()
word2 = input()

# 调用函数
print(shared_chars_count(word1, word2))
