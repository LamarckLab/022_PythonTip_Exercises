def max_adjacent(arr):
    # 此处编写代码
    target_lst = []
    for index in range(0,len(arr)-1):
        target_lst.append(max(arr[index],arr[index+1]))
    return target_lst
# 获取输入，转换为列表 
arr = list(map(int, input().split()))

# 调用函数，输出结果 
result = max_adjacent(arr)
print(result)