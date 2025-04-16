def find_all_factors(num):
    # 此处写你的代码
    result_list = []
    for item in range(1,num+1):
        if num % item == 0:
            result_list.append(item)
    return result_list

# 输入一个数字 
num = int(input())

# 调用函数 
print(find_all_factors(num))
