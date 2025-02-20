def is_plural(term):
    # 此处编写代码 
    if term[-1] == 's':
        return True
    else:
        return False
# 获取输入 
input_word = input()

# 调用函数并输出结果 
print(is_plural(input_word))