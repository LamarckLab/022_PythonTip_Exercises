def count_binary_ones(num):
    # 此处写你的代码
    return str(bin(num)).count("1")

# 从标准输入读取一个整数
num = int(input())
# 调用函数
print(count_binary_ones(num))
