def gcd(a, b):
    # 编写你的代码，找出两个数字的最大公约数
    gcd = min(a,b)
    while gcd >= 1:
        if a % gcd == 0 & b % gcd == 0:
            return gcd
        else:
            gcd -= 1
    return 1


def find_gcd_of_numbers(numbers_list):
    # 编写你的代码，找出数字列表的最大公约数
    gcd = min(numbers_list)
    flag = True
    while gcd >= 1:
        for element in numbers_list:
            if element % gcd != 0:
                flag = False
        if flag == True:
            return gcd
        else:
            flag == True
            gcd -= 1
    return 1
        


# 获取整数输入并转换为列表
numbers_list = list(map(int, input().split()))
# 调用函数
print(find_gcd_of_numbers(numbers_list))