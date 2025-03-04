def perform_arithmetic_operation(operation_string):
    # 此处编写代码
    operation_list = operation_string.split(" ")
    if "+" in operation_list:
        return int(operation_list[0]) + int(operation_list[2])
    elif "-" in operation_list:
        return int(operation_list[0]) - int(operation_list[2])
    elif "*" in operation_list:
        return int(operation_list[0]) * int(operation_list[2])
    elif "//" in operation_list:
        if int(operation_list[2]) == 0:
            return -1
        else:
            return int(operation_list[0]) // int(operation_list[2])



# 获取输入
operation_string = input()
# 调用函数
print(perform_arithmetic_operation(operation_string))