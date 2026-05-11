a="봄"
b="여름"

print(a,b,sep="과 ",end=" 끝\n")
# sep: 출력물 사이의 구분자
# end: 출력물 맨 끝에 붙는 문자

# for i in range(1,100,2): 1~99까지 2씩 증가

#구구단
dan=int(input("원하는 단 입력: "))
for i in range(1,10):
    print(dan,"*",i,"=",dan*i)

for i in range(2,10):
    print(i,"단")
    for j in range(1,10):
        print(i,"*",j,"=",i*j)

import time
print()
for k in range(10,0,-1): #10~1
    print(k)
    time.sleep(1) #1초간 일시 정지
print("발사!!")