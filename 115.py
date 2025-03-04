def is_consecutive_sequence(list1, list2):
    # 在这里编写你的代码
    target_lst = sorted(list1 + list2)
    for index in range(0,len(target_lst)-2):
        if target_lst[index] + 1 == target_lst[index+1]:
            continue
        else:
            return False
    return True

# 将整数输入转换为列表
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
# 调用函数
print(is_consecutive_sequence(list1, list2))