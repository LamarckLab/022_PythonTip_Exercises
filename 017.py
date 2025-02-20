def find_nth_smallest(numbers_list, n):
    # 此处编写你的代码
    new_list = sorted(numbers_list)
    if n > len(new_list):
        return None
    else:
        return new_list[n-1]

# 将输入的整数转换为列表
numbers_list = list(map(int, input().split()))
# 获取n的输入
n = int(input())
# 调用函数
print(find_nth_smallest(numbers_list, n))