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

import sys
user_pass = input("패스워드를 입력하시오(영어3자): ")
password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 
            'w', 'x', 'y', 'z',]
for letter1 in password:
        for letter2 in password:
            for letter3 in password:
                guess = letter1+letter2+letter3
                print(guess)
                if guess == user_pass:
                    print("당신의 패스워드는 "+guess)
                    sys.exit() #중지