def min_removals_to_anagram(str1, str2):
    # 此处编写代码
    lst1 = list(str1)
    lst2 = list(str2)
    for letter in str1:
        if letter in str2:
            lst1.remove(letter)
            lst2.remove(letter)
    return len(lst1) + len(lst2)

# 获取输入 
str1 = input()
str2 = input()

# 调用函数，输出结果 
print(min_removals_to_anagram(str1, str2))
