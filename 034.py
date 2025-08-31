def add_numbers(num1, num2):
    # 此处编写代码
    try:
        return int(num1) + int(num2)
    except:
        return "Invalid Operation"
# 获取用户输入num1 和 num2 
num1 = input()
num2 = input()

# 调用函数
result = add_numbers(num1, num2)

# 打印和
print(result)
