def convert_set_to_dict(input_set):
    # 此处写下你的代码
    input_set = sorted(input_set)
    target_dict = {}
    for element in input_set:
        target_dict[element] = 0
    return target_dict

# 获取输入，转为集合
input_set = set(map(int, input().split()))

# 调用函数 
print(convert_set_to_dict(input_set))