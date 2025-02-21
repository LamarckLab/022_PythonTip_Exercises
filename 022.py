def count_binary_ones(num):
    # 此处写你的代码
    bin_num = bin(num)
    str_num = str(bin_num)
    return str_num.count("1")

# 从标准输入读取一个整数
num = int(input())
# 调用函数
print(count_binary_ones(num))