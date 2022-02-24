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


## 값 비교
print(c == c[:3] + c[3:]) # True

## 같은 id 값
temp = c
print(c == temp) # True
print(id(c) == id(temp)) # True, 파이썬은 내부적으로 최적화를 해서 자료구조를 저장하고 있다.

## 리스트 수정 삭제
z = [1,2,3,4,5,6]
z[0] = 'a'
print(z) # ['a', 2, 3, 4, 5, 6]
z[1:2] = ['a','b','c'] 
print(z) # ['a', 'a', 'b', 'c', 3, 4, 5, 6]
z[1:3] = []
print(z) # ['a', 'c', 3, 4, 5, 6]
del z[3]
print(z) # ['a', 'c', 3, 5, 6]

## 리스트 함수
'''
myList = []

myList.append(1) // 마지막에 추가
myList.pop() // 마지막 요소 삭제
myList.sort() // 오름차순 정렬
myList.reverse() // 내림차순 정렬
myList.insert(index, value) // index 위치에 value 추가
myList.remove(value) // value 삭제
myList.index(value) // value 위치 확인
myList.count(value) // value 개수 확인
myList.clear() // 모든 요소 삭제
myList.copy() // 복사
myList.extend(list) // 리스트 연결

list 요소 삭제 : remove, pop, del
'''
myList = [1,'a',2,'c',3,'z',4,'o',5,'q',6]
strList = ['z', 'a', 'c', 'q', 'o']

myList.append(9)
print(myList) # [1, 'a', 2, 'c', 3, 'z', 4, 'o', 5, 'q', 6, 9]
myList.pop()
print(myList) # [1, 'a', 2, 'c', 3, 'z', 4, 'o', 5, 'q', 6]
strList.sort()
print(strList) # ['a', 'c', 'o', 'q', 'z']
myList.reverse()
print(myList) # [6, 'q', 5, 'o', 4, 'z', 3, 'c', 2, 'a', 1]
myList.insert(0, 0)
print(myList) # [0, 6, 'q', 5, 'o', 4, 'z', 3, 'c', 2, 'a', 1]
myList.remove('z')
print(myList) # [0, 6, 'q', 5, 'o', 4, 3, 'c', 2, 'a', 1]
myList.index('q')
print(myList.index('q')) # 2
myList.count('c')
print(myList.count('c')) # 1
myList.clear()
print(myList) # []
myList.append('a')
myList.extend([1,2,3,4,5])
print(myList) # ['a', 1, 2, 3, 4, 5]