def count_sublists(list_input):
    # 此处编写代码
    cnt = 0
    for element in list_input:
        if type(element) == list:
            cnt += 1
    return cnt

# 获取输入转为列表 
list_input = eval(input())

# 调用函数 
print(count_sublists(list_input))