import turtle #turtle 모듈 이용

t=turtle.Turtle() #turtle 객체 생성, t 변수에 할당
t.shape("turtle") #모양 설정

r=50 #반지름
t.circle(r) #원 그리기
t.fd(30) #앞으로 이동
t.circle(r) #원
t.fd(30) #앞으로 이동
t.circle(r) #원
t.fd(50) #앞으로 이동

for i in range(4):
    t.forward(2*r)
    t.right(90) #오른쪽 이동
#한 변의 길이가 지름인 정사각형 그리기

for i in range(3):
    t.forward(2*r)
    t.right(120) #오른쪽 이동
#한 변의 길이가 지름인 정삼각형 그리기