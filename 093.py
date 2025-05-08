def list_into_chunks(num_list, chunk_size):    
    # 此处编写代码
    output_list = []
    start_index = 0
    while start_index < len(num_list):
        output_list.append(num_list[start_index:start_index+chunk_size])
        start_index += chunk_size
    return output_list

# 从用户输入中获取数据，并将其转换为列表
num_list = list(map(int, input().split()))
# 从用户输入中获取块大小
chunk_size = int(input())
# 调用函数
print(list_into_chunks(num_list, chunk_size))
