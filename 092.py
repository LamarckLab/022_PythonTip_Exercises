def can_form_palindrome(word):
    # 在此处编写你的代码
    count_dict = {}
    count_odd = 0
    flag = True
    if len(word) % 2 == 0:
        for char in word:
            if char not in count_dict:
                count_dict[char] = 1
            else:
                count_dict[char] += 1
        for element in count_dict:
            if count_dict[element] % 2 != 0:
                flag = False
    else:
        for char in word:
            if char not in count_dict:
                count_dict[char] = 1
            else:
                count_dict[char] += 1
        for element in count_dict:
            if count_dict[element] % 2 != 0:
                count_odd += 1
        if count_odd > 1:
            flag = False
    return flag

# 从用户处获取输入
word = input()
# 调用函数
print(can_form_palindrome(word))