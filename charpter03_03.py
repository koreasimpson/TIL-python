# Chapter03 - 파이썬 기초 자료형
# Chapter03-1 - 리스트 자료형
# 자료구조에서 중요

'''
리스트 자료형은
1. 순서가 있다
2. 중복이 허용된다
3. 수정, 삭제가 가능하다
'''

## 선언
a = [] # <class 'list'>
b = list()
c = [5, 10 ,15]
d = [1000, 10000, 'Ace', 'Base', 'Captain']
e = [1, 10, 100, ['january', 'february', 'march']]
f = [21.42, 'footbar', 3, 4, False, 3.14159]

## 인덱싱
print('d : ', type(d), d) # d :  <class 'list'> [1000, 10000, 'Ace', 'Base', 'Captain']
print('d[1] : ', d[1]) # 10000
print('연산도 가능 : ', d[0] + d[1]) # 11000
print('배열 내 배열에 접근 : ', e[-1][1]) # february
print('문자를 배열로 변환 : ', list(e[-1][1])) # ['f', 'e', 'b', 'r', 'e', 'b', 'l', 'y']

##  슬라이싱
print('d[1:3] : ', d[0:3]) # [1000, 10000, 'Ace']
print(d[2:]) # ['Ace', 'Base', 'Captain']
print(e[-1][1:3]) # ['february', 'march']

## 리스트 연산
print(c + d) # [5, 10, 15, 1000, 10000, 'Ace', 'Base', 'Captain']
print(d + c) # [1000, 10000, 'Ace', 'Base', 'Captain', 5, 10, 15]
print(c * 3) # [5, 10, 15, 5, 10, 15, 5, 10, 15]
