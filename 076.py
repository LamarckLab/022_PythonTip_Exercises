def min_removals_to_anagram(str1, str2):
    # 此处编写代码
    list1, list2 = list(str1), list(str2)
    for letter in str1:
        if letter in str2:
            list1.remove(letter)
            list2.remove(letter)
    return len(list1)+len(list2)
# 获取输入 
str1 = input()
str2 = input()

# 调用函数，输出结果 
print(min_removals_to_anagram(str1, str2))
