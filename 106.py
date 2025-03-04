def find_missing_integer(number_list):
    # 此处写代码 
    max_digit = max(number_list)
    for digit in range(1,max_digit):
        if digit not in number_list:
            return digit
# 输入一串数字，以空格分隔，转换为列表
number_list = list(map(int, input().split()))
# 调用函数
print(find_missing_integer(number_list))