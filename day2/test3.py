to=int(input("투입한 돈: "))
price=int(input("물건 값: "))
# gu=to-price
# print("거스름돈:",gu)
# print("500원 동전의 개수:",gu//500)
# print("100원 동전의 개수:",gu%500//100)
change=to-price
coin500=change//500
change=change%500
coin100=change//100
print("500원 동전의 개수:",coin500)
print("100원 동전의 개수:",coin100)