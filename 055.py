def binary_to_decimal(binary_list):
     # 此处编写你的代码
     decimal_num = 0
     for i in range(1,len(binary_list)+1):
          decimal_num += binary_list[-1*i] * 2**(i-1)
     return decimal_num
# 获取输入，并转为列表 
binary_list = list(map(int, input().split()))

# 调用函数 
print(binary_to_decimal(binary_list))
