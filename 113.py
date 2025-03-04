def is_ordered_sublist(sublist, main_list):
    # 在这里编写你的代码
    while len(main_list) >= 1:
        if sublist[0] == main_list[0]:
            del main_list[0]
            del sublist[0]
            if len(sublist) == 0:
                return True
        else:
            del main_list[0]
    return False
    
# 将整数输入转换为主列表
main_list = list(map(int, input( ).split()))
# 将整数输入转换为子列表
sublist = list(map(int, input().split()))
# 调用函数
print(is_ordered_sublist(sublist, main_list))