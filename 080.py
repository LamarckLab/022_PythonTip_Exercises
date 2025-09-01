def convert_to_snake_case(s):
   # 此处编写代码
   output_s = ""
   for letter in s:
      if letter.islower():
         output_s += letter
      else:
         output_s += ("_"+letter.lower())
   return output_s
# 获取输入 
input_string = input()

# 调用函数，打印输出 
print(convert_to_snake_case(input_string))
