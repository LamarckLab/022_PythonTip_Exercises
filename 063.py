def max_gap(lst):
    # 此处编写代码
    target = 0
    lst = sorted(lst)
    for i in range(0,len(lst)-1):
        target = max(target, lst[i+1]-lst[i])
    return target

# 获取用户输入，转换为整数列表
numbers = list(map(int, input().split()))
# 调用函数，输出结果
print(max_gap(numbers))