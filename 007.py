def is_plural(term):
    # 此处编写代码
    return term[-1] == 's'

# 获取输入 
input_word = input()

# 调用函数并输出结果 
print(is_plural(input_word))
