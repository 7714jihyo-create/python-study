try:
    num=int(input("숫자 입력"))
    res=10/num
except ValueError:
    print("숫자가 아닙니다")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다")
except Exception as e:
    print('에러 메시지:',e)
else:
    print("결과:",res)
finally:
    print("종료")