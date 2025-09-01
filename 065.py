def merge_and_sort(first_list, second_list):
    # 此处编写代码
    if first_list == sorted(first_list):
        return sorted(first_list + second_list)
    else:
        return sorted(first_list + second_list)[::-1]
# 获取输入，转换为列表
first_list = list(map(int, input().split()))
second_list = list(map(int, input().split()))

# 调用函数
print(merge_and_sort(first_list, second_list))
