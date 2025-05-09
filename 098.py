def binary_anagram(num1, num2):
    # 此处编写代码
    bin_1 = bin(num1)[2:]
    bin_2 = bin(num2)[2:]
    return bin_1.count("1") == bin_2.count("1")

# 获取输入 
num1 = int(input())
num2 = int(input())

# 调用函数 
print(binary_anagram(num1, num2))
