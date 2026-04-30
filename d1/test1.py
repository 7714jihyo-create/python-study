name=input("이름: ")
price=int(input("가격: "))
quan=int(input("수량: "))

print(name+"의 총 가격은",(price*quan),"원 입니다.")
print(name+"의 총 가격은 "+str(price*quan)+"원 입니다.")
#숫자 문자로 변환할 때 str, 실수 float
print(name+"의 총 가격은 %d원 입니다." %(price*quan))
print(f"{name}의 총 가격은 {price*quan} 원 입니다")
#print 안에서 f는 f-string, 포맷 문자열 => f"{변수 값}""