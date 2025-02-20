def are_anagrams(string1, string2):
    # 此处编写代码 
    list1 = sorted(string1.lower().replace(" ",""))
    list2 = sorted(string2.lower().replace(" ",""))

    if list1 == list2:
        return True
    else:
        return False
    

# 获取输入string1 和 string2 
string1 = input()
string2 = input()
# 调用函数并打印结果 
print(are_anagrams(string1, string2))