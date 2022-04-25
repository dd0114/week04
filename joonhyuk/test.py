def foo(a):
    # 1. 파라미터와 매개변수 차이 확인
    print("Inside Function(1):",a, id(a))
    # 2. 파라미터를 변경했을 때
    a += ' very old'
    print("Inside Function(2):",a, id(a))
    # 3. 파라미터를 변경했을 때
    a = "new value"
    print("Inside Function(3):",a, id(a))
     
string = "old value"
foo(string)
print("Outside Function:", string, id(string))