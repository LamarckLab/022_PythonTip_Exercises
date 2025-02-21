def find_even_numbers(num):
    # 此处写入代码
    my_list = []
    if num <= 1:
        return my_list
    else:
        for i in range(1,num+1):
            if i % 2 == 0:
                my_list.append(i)
        return my_list

# 获取整数输入
num = int(input())
# 调用函数
print(find_even_numbers(num))