def can_form_target(list_of_lists, target_list):
    # 在这里编写你的代码
    sum_list = []
    for sub_list in list_of_lists:
        sum_list += sub_list
    return sorted(sum_list) == sorted(target_list)
# 获取用户输入
user_list_of_lists = [list(map(int, input().split())) for _ in range(int(input()))]
user_target_list = list(map(int, input().split()))

# 调用函数
print(can_form_target(user_list_of_lists, user_target_list))
