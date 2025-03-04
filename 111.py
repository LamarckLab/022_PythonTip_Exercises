def larger_than_following(num_list):
    # 此处写下你的代码
    target_lst = []
    length = len(num_list)
    flag = True
    for i in range(0,length-1):
        for j in range(i+1,length):
            if num_list[i] < num_list[j]:
                flag = False
        if flag:
            target_lst += [num_list[i]]
            i += 1
        else:
            flag = True
            i += 1
    return target_lst
# 获取输入，并将其转换为列表
num_list = list(map(int, input().split()))
# 调用函数
print(larger_than_following(num_list))