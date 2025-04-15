def list_between(start, end):
    # 此处写你的代码
    my_list = []
    for item in range(start+1, end):
        my_list.append(item)
    return my_list

# 获取输入的start 及 end
start = int(input())
end = int(input())

# 调用函数
print(list_between(start, end))
