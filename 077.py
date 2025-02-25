def letter_indices(word):
    # 此处编写代码
    mylst = list(word)
    target_dict = {}
    for index in range(len(mylst)):
        if mylst[index] not in target_dict:
            target_dict[mylst[index]] = [index]
        else:
            target_dict[mylst[index]] += [index]
    return target_dict


# 获取输入 
word = input()

# 调用函数 
print(letter_indices(word))