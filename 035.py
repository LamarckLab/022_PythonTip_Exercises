def hex_to_binary(hex_number):
    # 此处编写代码
    return bin(hex_number)[2:].zfill(8)
# 获取用户输入的16进制数
hex_number = int(input(), 16)

# 打印转换后的二进制数 
print(hex_to_binary(hex_number))
