def break_down_list(items):
    # 此处编写代码
    sub_dict = {}
    target_list = []
    while len(items) > 0:
        if items[0]["quantity"] > 0:
            sub_dict["type"] = items[0]["type"]
            sub_dict["quantity"] = 1
            target_list += [sub_dict]
            sub_dict = {}
            items[0]["quantity"] -= 1
        else:
            items = items[1:]
    return target_list
# 获取物品列表 
items = eval(input())
# 调用函数，输出分解后的物品列表
print(break_down_list(items))