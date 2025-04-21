def is_sum_present(num_list, target_sum):
    # 此处编写代码
    for letter1 in num_list:
        for letter2 in num_list:
            if letter1 + letter2 == target_sum and letter1 != letter2:
                return True
    return False

# 获取输入
num_list = list(map(int, input().split()))
target_sum = int(input())

# 调用函数 
print(is_sum_present(num_list, target_sum))
