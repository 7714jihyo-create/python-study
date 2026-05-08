str=input("영어 1글자 입력: ")

if('A'<=str<='Z'):
    print(str.lower())
elif('a'<=str<='z'):
    print(str.upper())
else:
    print("다시 입력")