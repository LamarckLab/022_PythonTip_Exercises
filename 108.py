def is_palindrome(n):
    return str(n) == str(n)[::-1]

# 定义函数
def find_closest_palindrome(num):
    # 在此处编写代码
    lower = num
    upper = num
    while True:
        if is_palindrome(lower):
            return lower
        if is_palindrome(upper):
            return upper
        lower -= 1
        upper -= 1

# 从用户处获取输入
num = int(input())
# 调用函数
print(find_closest_palindrome(num))