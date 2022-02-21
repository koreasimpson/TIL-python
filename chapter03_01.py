# Chapter03 - 파이썬 기초 자료형
# Chapter03-1 - 숫자형 사용법
# 파이썬 모든 자료형, 데이터 타입 선언, 연산자 활용, 형 변환, 외부 모듈 사용...

""" 파이썬 지원 자료형
int: 정수형
float: 실수형
complex: 복소수형
bool: 불린형(true/false)
str: 문자열(시퀀스)
list: 리스트(시퀀스)
tuple: 튜플(시퀀스)
set: 집합
dict: 사전
"""

str1 = 'Hello Python' # <class 'str'>
str2 = 'Anaconda' # <class 'str'>
bool1 = True # <class 'bool'>

int1 = 10 # <class 'int'>
float1 = 10.0 # <class 'float'> / 10과 10.0은 데이터 타입이 다르므로. 같지 않다

list = [str1, str2] # <class 'list'>
dict = { 'name':'Anaconda', 'age':10 } # <class 'dict'>
tuple1 = 4, 5, 6 # <class 'tuple'>
tuple2 = (7, 8, 9) # <class 'tuple'>
set = {3, 5, 7} # <class 'set'>


""" 숫자형 연산자

+ : 합
- : 뺄셈
* : 곱
/ : 나눗셈
// : 나눗셈의 몫
% : 나눗셈의 나머지
abs(x) : 절대값
pow(x, y) : x의 y제곱
x ** y : x의 y제곱

"""

int2 = 88
int3 = -100
big_int = 190231283018203810923709172095790172097309172390127095710927309127309172903710965901273091720937102937190231283018203810923709172095790172097309172390127095710927309127309172903710965901273091720937102937

f1 = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9

num1 = 39
num2 = 123
num3 = -1233
big_num1 = 129031902380192766666
big_num2 = 999746237137172371727
fnum1 = 1.234
fnum2 = 4.913

# 형이 다른 값을 연산하려고 할 때는 자동형 변환이 일어난다. ex) 정수(int) + 실수(float) = 실수(float)

# 형 변환 실습
a = 3.
b = 6
c = .7
d = 12.7
print(type(a), type(b), type(c), type(d)) # <class 'float'> <class 'int'> <class 'float'> <class 'float'>

print(float(b)) # 6.0
print(int(c)) # 0
print(int(d)) # 12
print(int(True)) # 1 / True : 1
print(float(False)) # 0.0 / False : 0
print(complex(3)) # (3+0j)
print(complex('3')) # (3+0j)  / 문자형 -> 숫자형
print(complex(False)) # 0j

# 수치 연산 함수
x, y = divmod(100, 8)
print(x, y) # 12, 4

# 외부 모듈
import math

print(math.pi) # 3.141592653589793
print(math.ceil(5.1)) # 6 / 올림