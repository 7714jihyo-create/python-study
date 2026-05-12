# [Global Scope] 전역 범위: 프로그램 어디서든 접근 가능
a = '홍길동'
b = 99

def function1():
    # [Enclosing Scope] 부모 함수 범위
    # 전역 변수 a와 이름은 같지만 function1 내부에서만 사용하는 별개의 'a'입니다.
    a = '이순신' 
    c = [1, 2, 3]
    
    def function2():
        # [Local Scope] 지역 범위: function2 내부
        d = (1, 2, 3)
        
        # LEGB 규칙에 따라 변수를 찾음
        print('Local a =', a) # Enclosing의 '이순신' 사용
        print('Local b =', b) # Global의 99 사용 (Local, Enclosing에 없으므로)
        print('Local c =', c) # Enclosing의 [1, 2, 3] 사용
        print('Local d =', d) # Local의 (1, 2, 3) 사용
        
    function2()
    
    print('Enclosing a =', a) # '이순신' 출력
    print('Enclosing b =', b) # 99 출력
    print('Enclosing c =', c) # [1, 2, 3] 출력
    
    # d는 function2의 지역 변수, function1에서 접근X
    # print('Enclosing d =', d) -> 에러

function1()

print('Global a =', a) # '홍길동' 출력 (전역 변수는 변하지 않음)
print('Global b =', b) # 99 출력

# c와 d는 각각 function1, function2 내부에서 생성된 지역 변수
# print('Global c =', c) -> 에러
# print('Global d =', d) -> 에러