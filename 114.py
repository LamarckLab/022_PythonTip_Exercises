def reorder_list_digits(num_list):
    # 此处写下你的代码
    target_lst = []
    single_num = ""
    for element in num_list:
        element = sorted(str(element))[::-1]
        for index in range(0,len(element)):
            single_num += element[index]
        target_lst += [int(single_num)]
        single_num = ""
    return target_lst     

# 获取输入的数字并转换为列表
num_list = list(map(int, input().split()))
# 调用函数
print(reorder_list_digits(num_list))