def find_largest_even(lst):
    # 此处编写你的代码
    max_even = -1
    for digit in lst:
        if digit % 2 == 0:
            max_even = max(max_even, digit)
    return max_even

# 获取输入转为整数列表 
input_list = list(map(int, input().split()))

# 调用函数 
print(find_largest_even(input_list))
