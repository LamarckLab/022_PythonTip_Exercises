def reverse_binary_integer(n):
    # 此处编写你的代码
    bin_n = bin(n)[2:]
    reversed_bin_n = bin_n[::-1]
    exponent = 0
    reversed_decimal_n = 0
    for digit in reversed_bin_n[::-1]:
        reversed_decimal_n += int(digit) * (2**exponent)
        exponent += 1
    return reversed_decimal_n
# 获取输入 
n = int(input())

# 调用函数 
print(reverse_binary_integer(n))
