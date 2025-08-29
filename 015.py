def is_string_identical(text_string):
    # 此处编写代码
    return len(set(text_string)) == 1
# 获取输入 
text_string = input()
# 调用函数 
print(is_string_identical(text_string))
