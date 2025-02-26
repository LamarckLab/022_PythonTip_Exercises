def list_into_chunks(num_list, chunk_size):    
    # 此处编写代码
    index = 0
    sub_list = []
    target_list =[]
    i = 0
    while i < len(num_list):
        index += 1
        if index <= chunk_size:
            sub_list += [num_list[i]]
            i += 1
        else:
            index = 0
            target_list.append(sub_list)
            sub_list = []
    if index > 0:
        target_list.append(sub_list)
    return target_list

    
    
# 从用户输入中获取数据，并将其转换为列表
num_list = list(map(int, input().split()))
# 从用户输入中获取块大小
chunk_size = int(input())
# 调用函数
print(list_into_chunks(num_list, chunk_size))