def find_all_factors(num):
    # 此处写你的代码 
    my_list = []
    for element in range(1, num+1):
        if num % element == 0:
            my_list.append(element)
    return my_list

# 输入一个数字 
num = int(input())

# 调用函数 
print(find_all_factors(num))