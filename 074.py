def sort_words_by_char(words, index):
    # 在此处编写代码
    for i in range(len(words)-1):
        for j in range(i+1, len(words)):
            if words[i][index-1] > words[j][index-1]:
                words[i], words[j] = words[j], words[i]
    return words
# 获取用户输入
words = input().split() # 单词列表
index = int(input())    # 位置

# 调用函数
print(sort_words_by_char(words, index))
