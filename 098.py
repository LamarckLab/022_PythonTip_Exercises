def binary_anagram(num1, num2):
    # 此处编写代码
    bin1 = bin(num1)[2:]
    bin2 = bin(num2)[2:]
    if bin1.count("1") == bin2.count("1"):
        return True
    else:
        return False
# 获取输入 
num1 = int(input())
num2 = int(input())

# 调用函数 
print(binary_anagram(num1, num2))