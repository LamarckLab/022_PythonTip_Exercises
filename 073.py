def can_form_target(list_of_lists, target_list):
    # 在这里编写你的代码
    list_len = len(list_of_lists)
    sum_list = []
    for lst in list_of_lists:
        sum_list += lst
    return set(target_list).issubset(sum_list)


# 获取用户输入
user_list_of_lists = [list(map(int, input().split())) for _ in range(int(input()))]
user_target_list = list(map(int, input().split()))

# 调用函数
print(can_form_target(user_list_of_lists, user_target_list))
