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
print(name)

print("python"*5)