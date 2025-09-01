def letter_indices(word):
    # 此处编写代码
    indices_dict = {}
    for index in range(len(word)):
        if word[index] not in indices_dict:
            indices_dict[word[index]] = [index]
        else:
            indices_dict[word[index]].append(index)
    return indices_dict
# 获取输入 
word = input()

# 调用函数 
print(letter_indices(word))
