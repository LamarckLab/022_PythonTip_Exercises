def is_almost_sorted(lst):
    # 此处编写代码
    target = []
    if lst == sorted(lst) or lst == sorted(lst)[::-1]:
        return -1
    for index in range(1,len(lst)):
        target = lst[:index] + lst[index+1:]
        if target == sorted(target) or target == sorted(target)[::-1]:
            return True
    return False
# 获取用户输入，并将其转换为列表
user_list = list(map(int,input().split()))
# 调用函数
print(is_almost_sorted(user_list))