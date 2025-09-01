def binary_to_int(bin_tuple):
    # 此处编写代码，bin_tuple 为元组
    decimal_num = 0
    for index in range(1,len(bin_tuple)+1):
        decimal_num += bin_tuple[-1*index] * 2**(index-1)
    return decimal_num
# 读取输入，将输入转换为元组 
bin_tuple = tuple(map(int,input().strip().split()))

# 调用函数binary_to_int()，并输出结果
print(binary_to_int(bin_tuple))
