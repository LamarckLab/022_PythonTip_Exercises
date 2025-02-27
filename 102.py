# 从itertools模块中导入combinations函数
from itertools import combinations

# 定义函数
def generate_subsets(input_set, n):
    # 在这里编写你的代码
    target_list = []
    for element in combinations(input_set,n):
        target_list += [set(element)]
    return target_list

# 输入整数并将其转换为集合
input_set = set(map(int, input().split()))
# 输入子集大小
n = int(input())
print(generate_subsets(input_set, n))