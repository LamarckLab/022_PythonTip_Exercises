def max_adjacent(arr):
    # 此处编写代码
    max_list = []
    for index in range(len(arr)-1):
        max_num = max(arr[index],arr[index+1])
        max_list.append(max_num)
    return max_list
# 获取输入，转换为列表 
arr = list(map(int, input().split()))

# 调用函数，输出结果 
result = max_adjacent(arr)
print(result)
