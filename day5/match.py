menu=int(input("메뉴 입력(1-입금 2-출력 기타-잔액 없음): "))

match menu:
    case 1:
        print("입금")
    case 2:
        print("출금")
    case _:
        print("잔액 없음")

num1=int(input("짝수 입력: "))
num2=int(input("홀수 입력: "))
match num1%2, num2%2:
    case 0,1:
        print("num1은 짝수, num2는 홀수")
    case 0,_:
        print("num1은 짝수, num2는 홀수가 아님")
    case _,1:
        print("num1은 짝수가 아님, num2는 홀수")
    case _,_:
        print("오류")

num1=int(input("3의 배수 입력: "))
num2=int(input("5의 배수 입력: "))
match num1%3, num2%5:
    case 0,0:
        print("num1은 3의 배수, num2는 5의 배수")
    case 0,_:
        print("num1은 3의 배수, num2는 5의 배수가 아님")
    case _,0:
        print("num1은 3의 배수가 아님, num2는 5의 배수")
    case _,_:
        print("오류")