def reverse_binary_integer(n):
    # 此处编写你的代码
    n_bin = bin(n)[2:]
    n_bin_reversed = n_bin[::-1]
    return int(n_bin_reversed, 2)


# 获取输入 
n = int(input())

# 调用函数 
print(reverse_binary_integer(n))