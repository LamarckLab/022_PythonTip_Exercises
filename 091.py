def count_palindromes(start_number, end_number):
    # 此处编写代码
    count = 0
    for num in range(start_number, end_number+1):
        if str(num) == str(num)[::-1]:
            count += 1
    return count

# 获取输入 
start_number = int(input())
end_number = int(input())
# 调用函数 
print(count_palindromes(start_number, end_number))
