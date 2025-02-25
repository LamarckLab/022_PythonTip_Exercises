def min_removals_to_anagram(str1, str2):
    # 此处编写代码
    common_lst = []
    lst1 = list(str1)
    lst2 = list(str2)
    lst2_copy = lst2
    for element in lst1:
        if element in lst2_copy:
            common_lst += element
            lst2_copy.remove(element)
    return len(str1) + len(str2) - 2*len(common_lst)

# 获取输入 
str1 = input()
str2 = input()

# 调用函数，输出结果 
print(min_removals_to_anagram(str1, str2))