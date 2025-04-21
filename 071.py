def smallest_multiple(digits, multiple_of):
    # 此处编写代码
    num = 10**(digits-1)
    while True:
        if num % multiple_of == 0:
            return num
        else:
            num += 1

# 获取输入 
digits = int(input())
multiple_of = int(input())

# 调用函数，输出结果 
print(smallest_multiple(digits, multiple_of))
