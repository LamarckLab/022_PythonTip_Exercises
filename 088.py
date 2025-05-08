def convert_set_to_dict(input_set):
    # 此处写下你的代码
    output_dict = {}
    input_lst = sorted(list(input_set))
    for element in input_lst:
        output_dict[element] = 0
    return output_dict
    
# 获取输入，转为集合
input_set = set(map(int, input().split()))

# 调用函数 
print(convert_set_to_dict(input_set))
