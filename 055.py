def binary_to_decimal(binary_list):
     # 此处编写你的代码 
     exponent = 0
     decimal = 0
     for digit in binary_list[::-1]:
          decimal += digit * (2**exponent)
          exponent += 1
     return decimal
# 获取输入，并转为列表 
binary_list = list(map(int, input().split()))

# 调用函数 
print(binary_to_decimal(binary_list))
