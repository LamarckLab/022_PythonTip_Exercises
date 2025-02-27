# 定义函数
def extract_max_min(input_tuple, k):
    # 对输入元组进行排序
    sorted_tuple = sorted(input_tuple)
    # 在此处编写你的代码
    return tuple(sorted_tuple[:k] + sorted_tuple[-k:])

# 获取整数输入并将其转换为元组
input_tuple = tuple(map(int, input().split()))
# 获取K的值
k = int(input())
# 调用函数
print(extract_max_min(input_tuple, k))