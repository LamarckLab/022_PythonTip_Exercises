# 定义函数
def extract_max_min(input_tuple, k):
    # 在此处编写你的代码
    input_list = sorted(list(input_tuple))
    output_list = input_list[:k] + input_list[len(input_list)-k:]
    return tuple(output_list)
    
# 获取整数输入并将其转换为元组
input_tuple = tuple(map(int, input().split()))
# 获取K的值
k = int(input())
# 调用函数
print(extract_max_min(input_tuple, k))
