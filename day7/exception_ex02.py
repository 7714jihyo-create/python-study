fruits=['사과','배','오렌지']

try:
    index = int(input("번호 입력: "))
    if index<0 or index>len(fruits)-1:
        raise IndexError #강제로 예외 발생
except IndexError:
    print("없는 인덱스입니다")
except ValueError:
    print("입력 오류")
except Exception as e:
    print('에러 메시지:',e)
else:
    print(fruits[index])
finally:
    print('종료')