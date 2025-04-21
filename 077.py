def letter_indices(word):
    # 此处编写代码
    output_dict = {}
    for index in range(len(word)):
        if word[index] not in output_dict:
            output_dict[word[index]] = [index]
        else:
            output_dict[word[index]] += [index]
    return output_dict

# 获取输入 
word = input()

# 调用函数 
print(letter_indices(word))
