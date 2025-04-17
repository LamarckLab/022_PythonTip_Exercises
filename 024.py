def find_even_numbers(num):
    # 此处写入代码
    my_list = []
    for item in range(2, num+1):
        if item % 2 == 0:
            my_list.append(item)
    return my_list

# 获取整数输入
num = int(input())
# 调用函数
print(find_even_numbers(num))
