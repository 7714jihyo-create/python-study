s="Hello Python"
print(s[6]) #인덱싱
print(s[6:12]) #슬라이싱

jumin="081111-4123456"
print("성별: "+jumin[7])
print(jumin[2:4]+"월"+jumin[4:6]+"일")
print(jumin[-7:])

s1="나는 학생입니다"
s2="파이썬을 배웁니다"
s3='재밌습니다'
s4=""" 
    나는 학생입니다
    파이썬을 배웁니다
    재미있습니다
""" #여러 문자열 저장할 때, 입력한 그대로 저장
print(s4)

year="1970"
month="05"
day="20"
date=year+"-"+month+"-"+day
print(date)

date2=date.split('-')
print(date2)
print(type(date2))
print(date2[1][0:2], end="*")

name="kakao taxi"
name2=name.replace("k","t",1)
print()
print(name2)

print("python"*5) #반복

#콤마 제거
won="63,120,450"
won2=won.replace(",","")
print(won2)

won3=3459088
won4=format(won3, " ,d")
print(won4)

#문자열 대소문자, 길이
p="Python is Amaizing"
print(p.lower) #소문자
print(p.upper) #대문자
print(p.capitalize)
print(p[0].isupper)
print(len(p))
print(p.count("i"))

#위치
index=p.index("i")
print(index)
index=p.index("i",index+1)
print(index)

#answkduf dusruf
words=["Python","is","easy"]
result=" ".join(words)
print(result)

#제거
text="  Hello   Python  "
print(text.strip())
print(text.rstrip('*'))

#자리수만큼 0으로 채우기
num="5"
result=num.zfill(3)
print(result)

#format
age=19
print("나는 %d살입니다" %age)
print("나는 {}살 입니다".format(age))

like="노래 부르기"
print("나는 %d살이고 %s를 좋아해요" %(age,like))
print("나는 {1}살이고 {0}를 좋아해요".format(age,like))
# fstring
print(f"나는 {age}살이고 {like}를 좋아해요")

print("나의 주소는 {addr}이며 나의 키는 {height}cm입니다".format(addr="인천",height=165))

#이스케이프 문자
print("\n배우는 과목은\n \"파이썬\" 입니다")
#\r 커서를 맨 앞으로 이동
print("red apple\rpine") 
print("i like you!\r!!") #\b 한 글자 삭제(backspace)
print("red\t apple") #\t 행 이동 (tab)

#인덱스 찾기
print(p.find("A")) #왼쪽부터 찾아서 인덱스 번호 출력
print(p.rfind("A")) #오른쪽부터
print(p.index("a")) #왼쪽부터 찾아서 인덱스 번호 출력
print(p.rindex("a")) #오른쪽부터

print(p.find("java")) #없는 문자를 찾으면 -1
#print(p.index("java")) 없는 문자를 찾으면 에러 발생

arr_Str=input("Input String: ").split("-")
#information-technology 입력, - 기준으로 information=[0] technology=[1]
arr_Len=int(input("Input Number: ")) #12 입력
arr_Val=list(range(0,arr_Len,2)) # [0, 2, 4, 6, 8, 10]
arr_Val.remove(4) # [0, 2, 6, 8, 10]
print(arr_Str[1].find('i')+arr_Val[2])
# i 없으므로 arr_Str[1].find('i')=-1, arr_Val[2]=6 -> -1+6=5