class Passbook:
    def __init__(self,owner,balance):
        self.owner=owner #예금주
        self.balance=balance #초기 잔액

    def deposit(self,money):
        self.balance+=money
        print(money,"원 입금 완료")
        print("현재 잔액은",self.balance,"원")

    def withdraw(self,money):
        if money<=self.balance: # 출금 금액은 잔액과 동일하거나 적어야 함
            self.balance-=money
            print(money,"원 출금")
            print("현재 잔액은",self.balance,"원")
        else:
            print("잔액 부족 출금 불가")

    def showInfo(self):
        print("예금주: ",self.owner)
        print("현재 잔액: ",self.balance)

class MinusPassbook(Passbook): #상속
    #withdraw() 오버라이딩
    def withdraw(self, money):
        if (self.balance-money)>=-1000000:
            self.balance-=money
            print(money,"원 출금")
            print("현재 잔액은",self.balance,"원")
        else:
            print("마이너스 한도 잔액 부족")
# 실행
# 객체 생성 account1
account1=Passbook("홍길동",100000)
account1.showInfo()
account1.deposit(50000)
account1.withdraw(120000)
account1.withdraw(70000)

account2=MinusPassbook("김철수",100000)
account2.showInfo()
account2.withdraw(200000)
account2.withdraw(950000)