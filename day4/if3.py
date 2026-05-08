num1=int(input("첫 번째 숫자를 입력: "))
num2=int(input("두 번째 숫자를 입력: "))
num3=int(input("세 번째 숫자를 입력: "))

if num1 >= num2 and num1 >= num3:
    biggest = num1
elif num2 >= num1 and num2 >= num3:
    biggest = num2
else:
    biggest = num3

print("제일 큰 수는", biggest)

# if(num1<num2):
#     if(num2<num3):
#         print("제일 큰 수는",num3)
#     else:
#         print("제일 큰 수는",num2)
# elif(num2<num1):
#     if(num1<num3):
#         print("제일 큰 수는",num3)
#     else:
#         print("제일 큰 수는",num1)