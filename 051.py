def add_space_before_capital(word):
    # 在此处编写你的代码
    cnt = 0
    while cnt < len(word):
        if word[cnt].isupper():
            word = word[:cnt] + " " + word[cnt:]
            cnt += 1
        cnt += 1
    return word.lower()

# 获取用户输入
word = input()

# 调用函数
print(add_space_before_capital(word))