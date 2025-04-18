def count_sublists(list_input):
    # 此处编写代码
    count = 0
    for sub_lst in list_input:
        if type(sub_lst) == list:
            count += 1
    return count
# 获取输入转为列表 
list_input = eval(input())

# 调用函数 
print(count_sublists(list_input))
