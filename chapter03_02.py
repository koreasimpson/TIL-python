# Chapter03 - 파이썬 기초 자료형
# Chapter03-1 - 문자형 사용법

# 문자열 생성
str1 = 'Hello Python'
str2 = "Anaconda"
str3 = """이것도 가능해"""
str4 = '''이것도 가능하구나'''

## len() 함수 : 문자열의 길이를 구하는 함수
print(len(str1)) # 12

## 빈 문자열 : '' 또는 "", str()
str_t1 = ''
str_t2 = str()
print(type(str_t2)) # <class 'str'>
print(len(str_t2)) # 0

## 이스케이프 문자 사용
""" Escape 코드
\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
"""
print("I'm Boy") # I'm boy
print('I\'m boy') # I'm boy
print('a \t b') # a        b
print('a \n b') #a 
                # b

## Raw String : r'', ''안의 내용을 그대로 출력
raw_s1 = r'D:\python\test'
print(raw_s1) # D:\python\test

## 멀티라인 입력
multi_str = '''
멀티라인을
입력해볼게요
과연 이게 문자열인가요?
'''
print(multi_str)

multi_str2 = \
'''
역 슬래시(\)를 사용하면
개행을 할 수 있다
개행한 다음의 내용이 변수에 할당된다.
'''
print(multi_str2)

## 문자열 연산
### 시퀀스는 'in' 과 'not in' 연산을 지원한다.
str_o1 = 'Hello'
str_o2 = 'Python'
str_o3 = 'How are you?'

print ('a' not in str_o1) # True
print('p' in str_o2) # False
print('P' in str_o2) # True
print('?' in str_o3) # True

## 문자열 형 변환 : 문자형으로 변환하고 싶으면 str() 함수를 사용한다.
is_str1 = str(123)
is_str2 = str(True)
is_str3 = str(3.14)
print (type(is_str1)) # <class 'str'>
print (type(is_str2)) # <class 'str'>
print (type(is_str3)) # <class 'str'>

## 문자열 함수
'''
upper() : 대문자로 변환
capitalize() : 첫번째 문자를 대문자로 변환
isalpha() : 문자만 있는지 확인
isalnum() : 문자와 숫자만 있는지 확인
startswith() : 문자열의 시작이 무엇인지 확인
endwith() : 문자열의 끝이 무엇인지 확인
count() : 문자열에 몇 개의 문자가 있는지 확인
replace(old, new) : old -> new 문자열을 변경한다.
split() : 문자열을 구분자로 나누어 리스트로 반환한다.
sorted() : 문자열을 정렬한다. (a-z 순서대로)
...
'''

## 반복(시퀀스)
im_str = 'Good Boy!'
print(dir(im_str)) # dir(str) : 문자열 객체에 정의된 함수를 보여준다. __iter__가 포함되어 있기 때문에 반복(시퀀스)이 가능하다.
for i in im_str:
    print(i)

## 슬라이싱 연습
str_s1 = "Hello Python"
print(str_s1[4]) # o
print(str_s1[-1]) # n
print(str_s1[-3]) # h
print(str_s1[0:3]) # Hel
print(str_s1[:3]) # Hel
print(str_s1[3:]) # lo Python
print(str_s1[:len(str_s1)]) # Hello Python
print(str_s1[:len(str_s1) - 1]) # Hello Pytho
print(str_s1[1:9:3]) # eoy, 3번째는 간격
print(str_s1[-5:]) # ython
print(str_s1[1:-2]) # ello Pyth
print(str_s1[::2]) # HloPto
print(str_s1[::-1]) # nohtyP olleH

## 아스키 코드(ASCII) 또는 유니코드(Unicode)
'''
ord() : 문자를 아스키 코드로 변환
chr() : 아스키 코드를 문자로 변환
'''

a = 'z'
print(ord(a)) # 122
print(chr(122)) # z