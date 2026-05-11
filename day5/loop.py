#1~100 중 5의 배수 제외한 합계
total=0
for i in range(0,101):
    if i%5!=0:
        total+=i
print(total)

# total=0
# for i in range(0,101):
#     if i%5==0:
#       continue #조건으로 이동
#     total+=i
# print(total)