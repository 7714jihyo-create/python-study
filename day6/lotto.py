import random

def get_lotto():
    numbers=[]
    while len(numbers)<7:
        n=random.randint(1,45) #무작위 수 발생 (1~45)
        if n not in numbers: #중복 방지
            numbers.append(n)
    return numbers 
 
print(f"로또 번호는 {get_lotto()}입니다")
