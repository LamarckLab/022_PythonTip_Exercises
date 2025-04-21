def binary_to_int(bin_tuple):
    # 此处编写代码，bin_tuple 为元组
    decimal_output = 0
    for i in range(len(bin_tuple)):
        decimal_output += bin_tuple[-i-1] * (2**i)
    return decimal_output

# 读取输入，将输入转换为元组 
bin_tuple = tuple(map(int,input().strip().split()))

# 调用函数binary_to_int()，并输出结果
print(binary_to_int(bin_tuple))
