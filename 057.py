def binary_to_int(bin_tuple):
    # 此处编写代码，bin_tuple 为元组
    target = 0
    for cnt in range(0,len(bin_tuple)):
        target += 2**cnt*bin_tuple[-cnt-1]
    return target
# 读取输入，将输入转换为元组 
bin_tuple = tuple(map(int,input().strip().split()))

# 调用函数binary_to_int()，并输出结果
print(binary_to_int(bin_tuple))