snack={
    "새우깡":3000,
    "매운 새우깡":3500,
    "양파링":4000
}
for i in snack.keys:
    print(i)
for j in snack.items:
    print(j)
for k in snack.values:
    print(k)

#리스트
fruit=["파인애플","참외","배","오렌지","골드키위"]
cart=[]
for i in fruit:
    if len(i)>=3:
        cart.append(i)
print(cart)