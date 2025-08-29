def are_anagrams(string1, string2):
    # 此处编写代码
    string1 = string1.lower().replace(" ","")
    string2 = string2.lower().replace(" ","")
    return sorted(string1) == sorted(string2)
# 获取输入string1 和 string2 
string1 = input()
string2 = input()
# 调用函数并打印结果 
print(are_anagrams(string1, string2))
