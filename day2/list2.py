movie_list=['아바타','왕사남','살목지','극한직업']
print(movie_list)

movie_list.insert(1,"범죄도시") #삽입
print(movie_list)

movie_list.append("슈퍼맨") #추가
print(movie_list)

movie_list.remove("살목지") #값 삭제
print(movie_list) 

#del: 명령어
del movie_list[2]
print(movie_list) #인덱스 지정 삭제

x=10
print(x)
del x
# print(x) 

print(len(movie_list)) #len: 길이

a=[1,2,3]
print(sum(a))

b=[90,50,80,70,55]
print(sum(b)/len(b))

#tuple: 나열, 리스트와 유사하나 값 변경 불가
tuple1=(1,2,3,4)
print(tuple1)
print(tuple1[2])
# tuple1[3]=50 -> 값 변경 안됨
# print(tuple1)