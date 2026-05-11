#디폴트인수: 함수를 정의할 때 매개변수에 기본값을 미리 설정

def greet(name,msg="별 일 없지?"):
    print("안녕 "+name+", "+msg)

greet("홍길동")

def print_star(n=1):
    print("n=",n)
    for i in range(n):
        print("**********")
print_star()
print_star(3)
