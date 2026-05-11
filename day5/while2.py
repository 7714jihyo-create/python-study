a=True #True=1

while a: # 일단 무한 루프
    a = int(input("숫자 입력(0 종료): "))
    if a == 0: # 0이면 즉시 탈출
        break
    print(a)
print("반복문 종료")

print("="*20)

menu=["쫄면","김밥","냉면","어묵"]
b=input("메뉴 선택")
while b in menu:
    print(b)
    b=input("메뉴 선택: ") #b 초기화
    
