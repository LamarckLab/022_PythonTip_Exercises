def reverse_binary_integer(n):
    # 此处编写你的代码
    return int(bin(n)[2:][::-1],2)
# 获取输入 
n = int(input())

# 调用函数 
print(reverse_binary_integer(n))
