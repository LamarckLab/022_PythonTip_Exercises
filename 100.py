def break_down_list(items):
    # 此处编写代码
    output_list = []
    for sub_dict in items:
        while sub_dict['quantity'] > 0:
            temp_dict = sub_dict.copy()
            temp_dict['quantity'] = 1
            output_list.append(temp_dict)
            sub_dict['quantity'] -= 1
    return output_list

# 获取物品列表 
items = eval(input())
# 调用函数，输出分解后的物品列表
print(break_down_list(items))
