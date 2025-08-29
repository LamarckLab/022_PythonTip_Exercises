def find_all_factors(num):
    # 此处写你的代码
    factor_list = []
    for i in range(1,num+1):
        if num % i == 0:
            factor_list.append(i)
    return factor_list
# 输入一个数字 
num = int(input())

# 调用函数 
print(find_all_factors(num))
