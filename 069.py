def is_sum_present(num_list, target_sum):
    # 此处编写代码
    for i in range(len(num_list)-1):
        for j in range(i+1,len(num_list)):
            if num_list[i] + num_list[j] == target_sum:
                return True
    return False
# 获取输入
num_list = list(map(int, input().split()))
target_sum = int(input())

# 调用函数 
print(is_sum_present(num_list, target_sum))
