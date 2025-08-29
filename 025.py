def find_first_n_odds(n):
    # 此处写你的代码
    odds_list = []
    for i in range(n):
        odds_list.append(i*2+1)
    return odds_list
# 获取输入n
n = int(input())
# 调用函数
print(find_first_n_odds(n))
