def add_numbers(num1, num2):
    # 此处编写代码 
    if num1 == "" or num1 == "None" or num2 == "" or num2 == "None":
        return "Invalid Operation"
    else:   
        my_sum = int(num1) + int(num2)
        return str(my_sum)

# 获取用户输入num1 和 num2 
num1 = input()
num2 = input()

# 调用函数
result = add_numbers(num1, num2)

# 打印和
print(result)