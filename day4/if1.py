#점수에 따른 학점
score=int(input("점수를 입력하세요: "))

if(80<score<=100):
    print("A")
elif(60<score):
    print("B")
elif(40<score):
    print("C")
elif(20<score):
    print("D")
else:
    print("E")