# Chapter02-2 
# 파이썬 완전 기초
# 파이썬 변수

# 기본 선언
num1 = 700
str1 = 'Hello'

print(num1)
print(type(num1)) # <class 'int'>, type(변수) : 변수의 자료형을 보여준다.
print(str1)
print(type(str1)) # <class 'str'>

# 동시 선언
x = y = z = 300

print(x, y, z)

# 재선언
k = 75
k = 'Hello K'

print(k)

# Object References
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# 예제1
print(300)
print(int(300))

# 예제2
a = 777
print(a) # <class 'int'>, 777

# 예제3
# 특정 변수의 값을 할당할 때는, 할당했을 당시의 값을 할당한다. 이후에 특정 변수의 값이 변해도, 그 값을 그대로 유지한다.
b = a
a = 888
print(a) # <class 'int'>, 888
print(b) # <class 'int'>, 777

# id(identity) : 객체의 고유값 확인

print(id(a)) # 4452267376
print(id(b)) # 4452267248
print(id(a) == id(b)) # False

# x = y = z = 300인 경우,
# 변수에 똑같은 값을 할당한다면 파이썬은 내부에서 하나만 만들어 진다.(중복된 객체를 만들지 않는다.)
print(id(x)) # 4502369488
print(id(y)) # 4502369488
print(id(z)) # 4502369488
print(id(x) == id(y) == id(z)) # True

i = 10
j = 11

print(id(i))
print(id(j))

i = 10
j = 10

print(id(i))
print(id(j))

i = j = 10
print(id(i))
print(id(j))

q = 10
print(id(q))