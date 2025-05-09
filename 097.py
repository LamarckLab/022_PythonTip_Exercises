def get_all_permutations(digits):
    # 在此处编写你的代码
    pmtt_list = [[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]]
    for pmtt in pmtt_list:
        print(digits[pmtt[0]], digits[pmtt[1]], digits[pmtt[2]])
    return None

# 获取整数输入并将其转换为列表
digits = list(map(int, input().split()))
# 调用函数
get_all_permutations(digits)
