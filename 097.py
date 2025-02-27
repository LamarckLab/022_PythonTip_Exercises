def get_all_permutations(digits):
    # 在此处编写你的代码
    target_list = []
    index_sort = ["012","021","102","120","201","210"]
    for i in range(0,6):
        for j in range(0,3):
            target_list += [digits[int(index_sort[i][j])]]
        print(target_list[0], target_list[1], target_list[2])
        target_list = []
            

# 获取整数输入并将其转换为列表
digits = list(map(int, input().split()))
# 调用函数
get_all_permutations(digits)