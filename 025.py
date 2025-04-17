def find_first_n_odds(n):
    # 此处写你的代码
    my_list = []
    for i in range(1,n+1):
        digit = 2*i - 1
        my_list.append(digit)
    return my_list


# 获取输入n
n = int(input())
# 调用函数
print(find_first_n_odds(n))
