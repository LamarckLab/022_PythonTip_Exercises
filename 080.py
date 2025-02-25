def convert_to_snake_case(s):
   # 此处编写代码
   for index in range(len(s)):
      if s[index].isupper():
         s = s[:index] + "_" + s[index].lower() + s[index+1:len(s)]
         index += 2
   return s

# 获取输入 
input_string = input()

# 调用函数，打印输出 
print(convert_to_snake_case(input_string))