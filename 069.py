def is_sum_present(num_list, target_sum):
    # 此处编写代码
    for i in range(0,len(num_list)):
        for j in range(0,len(num_list)):
            if i == j:
                continue
            else:
                if num_list[i] + num_list[j] == target_sum:
                    return True
    return False
# 获取输入
num_list = list(map(int, input().split()))
target_sum = int(input())

# 调用函数 
print(is_sum_present(num_list, target_sum))