def find_even_numbers(num):
    # 此处写入代码
    even_list = []
    for element in range(2,num+1):
        if element % 2 == 0:
            even_list.append(element)
    return even_list
# 获取整数输入
num = int(input())
# 调用函数
print(find_even_numbers(num))
