def is_sorted_rotated(input_list):
    # 此处写你的代码
    sorted_list = sorted(input_list)
    if input_list == sorted_list:
        return False
    for i in range(0,len(input_list)):
        input_list = input_list[1:] + [input_list[0]]
        if input_list == sorted_list:
            return True
    return False

# 获取输入，将输入转换成列表
input_list = list(map(int,input().split()))
# 调用函数
print(is_sorted_rotated(input_list))