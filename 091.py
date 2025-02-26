def count_palindromes(start_number, end_number):
    # 此处编写代码
    target_lst = []
    for num in range(start_number,end_number+1):
        if str(num) == str(num)[::-1]:
            target_lst += [num]
    return len(target_lst)

# 获取输入 
start_number = int(input())
end_number = int(input())
# 调用函数 
print(count_palindromes(start_number, end_number))