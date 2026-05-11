#함수
def add(a,b):
    return a+b
n1=int(input("숫자1 입력: "))
n2=int(input("숫자2 입력: "))    

print(add(n1,n2))

#숫자 리스트의 평균 반환하기
#1 리스트 합계 구하기
#2 리스트 개수 구하기
#3 합계/개수 반환

def avg(num):
    if not num:
        return 0  
    total=sum(num)
    cnt=len(num)
    return total/cnt
score_list=[80,90,100,50,70]
print(avg(score_list))
