def find_first_n_odds(n):
    # 此处写你的代码 
    my_list = []
    for i in range(1, 2*n):
        if i % 2 == 1:
            my_list.append(i)
    return my_list

# 获取输入n
n = int(input())
# 调用函数
print(find_first_n_odds(n))
