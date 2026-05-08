#주민번호로 성별 판별

rrn=input("주민등록번호 입력: ")

if(rrn[7]=='2' or rrn[7]=='4'):
    print("여자")
elif(rrn[7]=='1' or rrn[7]=='3'):
    print("남자")
else:
    print("다시 입력")

rrn=input("주민등록번호 입력: ").split("-")

if(rrn[1][0]=='2' or rrn[1][0]=='4'):
    print("여자")
elif(rrn[1][0]=='1' or rrn[1][0]=='3'):
    print("남자")
else:
    print("다시 입력")

rrn=input("주민등록번호 입력: ").split("-")[1]

if(rrn[0]=='2' or rrn[0]=='4'):
    print("여자")
elif(rrn[0]=='1' or rrn[0]=='3'):
    print("남자")
else:
    print("다시 입력")
