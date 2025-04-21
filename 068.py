def max_adjacent(arr):
    # 此处编写代码
    output_lst = []
    for i in range(len(arr)-1):
        output_lst += [max(arr[i],arr[i+1])]
    return output_lst

# 获取输入，转换为列表 
arr = list(map(int, input().split()))

# 调用函数，输出结果 
result = max_adjacent(arr)
print(result)
