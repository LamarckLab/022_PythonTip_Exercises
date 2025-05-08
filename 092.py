def can_form_palindrome(word):
    # 在此处编写你的代码
    odd_count = 0
    for letter in word:
        if word.count(letter) % 2 == 1:
            odd_count += 1
    return odd_count <= 1

# 从用户处获取输入
word = input()
# 调用函数
print(can_form_palindrome(word))
