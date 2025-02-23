def smallest_multiple(digits, multiple_of):
    # 此处编写代码
    num_start = 10**(digits-1)
    flag = True
    while flag:
        if num_start % multiple_of == 0:
            flag = False
            return num_start
        else:
            num_start += 1

# 获取输入 
digits = int(input())
multiple_of = int(input())

# 调用函数，输出结果 
print(smallest_multiple(digits, multiple_of))