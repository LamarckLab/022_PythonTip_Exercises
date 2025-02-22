def binary_to_decimal(binary_list):
     # 此处编写你的代码
     cnt = 1
     target = 0
     while cnt < len(binary_list)+1:
        target += 2**(cnt-1)*binary_list[-cnt]
        cnt += 1
     return target

# 获取输入，并转为列表 
binary_list = list(map(int, input().split()))

# 调用函数 
print(binary_to_decimal(binary_list))