# Today I Learned

<details>
<summary>template</summary>
<div>

### 제목

#### 부제목1

- 부제목 내용

```python
code
```

</div>
</details>

---

<details>
<summary>1일차 학습 요약</summary>
<div>

### Print

#### Separator 사용

- 콤마(,)로 구분된 문자열에 separator를 적용하여 출력

```python
    print("P", "Y", "T", "H", "O", "N", sep='')
    // PYTHON
    print("P", "Y", "T", "H", "O", "N", sep='-')
    // P-Y-T-H-O-N
```

#### End 사용

- print 내용간 줄바꿈이 되어 출력되지 않고, end 옵션의 내용 다음에 같은 라인에서 출력된다.

```python
    print('Welcome to', end='')
    print(' Python', end='     last')
    print('!')
    // Welcome to Python     last!
```

#### Python Format 사용

- format 옵션(d, s, f, ...) // d: digit, s: string, f: float, ...
- format 옵션을 사용하면 출력되는 문자열을 자동으로 포맷팅하여 출력한다.

```python
    print('%s %s' % ('one', 'two'))
    // one two

    print('{} {}'.format('one', 'two'))
    // one two
```

</div>
</details>

---

<details>
<summary>2일차 학습 요약</summary>
<div>

### 변수

#### 기본 선언

- 파이썬에서는 변수 키워드가 없다 (var, let, const 등등..)
- 파이썬에서 변수는 동적 타입이다

```python
num1 = 100
str1 = 'Hello'
```

#### 자료형

- <code>type(n)</code> : 변수의 자료형을 확인

```python
num1 = 700
str1 = 'Hello'

print(type(num1)) # <class 'int'>
print(type(num1)) # <class 'str'>
```

#### 값 복사

- 파이썬에서는 값 참조가 아닌 값 복사가 된다.

```python
a = 777
print(a) # 777

b = a
a = 888
print(a) # 888
print(b) # 777 # 이후에 a의 값이 변해도, b는 할당된 그 값을 그대로 유지한다.
```

#### id(identity)

- <code>id(변수)</code> : 객체의 고유값 확인
- 파이썬은 중복된 객체를 만드려고 하지 않는다. 이미 기존에 할당된 값을 새로운 변수에 담으려고 하는 경우 새로운 변수의 id는 기존에 할당된 값을 갖고 있는 변수의 id와 동일한 값을 갖게 된다.
- 그 이후에 기존에 없던 새로운 값이 할당되면 새로운 id를 갖게 된다.

```python
a = 888
b = 777
print(id(a)) # 4452267376
print(id(b)) # 4452267248
print(id(a) == id(b)) # False

x = y = z = 300
print(id(x)) # 4502369488
print(id(y)) # 4502369488
print(id(z)) # 4502369488
print(id(x) == id(y) == id(z)) # True

i = 10
j = 11

print(id(i)) # 4345625168
print(id(j)) # 4345625200
print(id(i) == id(j)) # False

i = 10
j = 10

print(id(i)) # 4345625168
print(id(j)) # 4345625168
print(id(i) == id(j)) # True

q = 10
print(id(q)) # 4319165008
```

</div>
</details>

---

<details>
<summary>3일차 학습 요약</summary>
<div>

### 파이썬 기초 자료형

#### 숫자형

파이썬 지원 자료형

- int: 정수형
- float: 실수형
- complex: 복소수형
- bool: 불린형(true/false)
- str: 문자열(시퀀스)
- list: 리스트(시퀀스)
- tuple: 튜플(시퀀스)
- set: 집합
- dict: 사전

```python
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
```

숫자형 연산자

- \+ : 합
- \- : 뺄셈
- \* : 곱
- / : 나눗셈
- // : 나눗셈의 몫
- % : 나눗셈의 나머지
- abs(x) : 절대값
- pow(x, y) : x의 y제곱
- x \*\* y : x의 y제곱

형이 다른 값을 연산하려고 할 때는 자동형 변환이 일어난다.
ex) 정수(int) + 실수(float) = 실수(float)

```python
a = 3.
b = 6
c = .7
d = 12.7
print(type(a), type(b), type(c), type(d))
# <class 'float'> <class 'int'> <class 'float'> <class 'float'>

print(float(b)) # 6.0
print(int(c)) # 0
print(int(d)) # 12
print(int(True)) # 1 / True : 1
print(float(False)) # 0.0 / False : 0
print(complex(3)) # (3+0j)
print(complex('3')) # (3+0j)  / 문자형 -> 숫자형
print(complex(False)) # 0j

x, y = divmod(100, 8)
print(x, y) # 12, 4
```

외부 모듈 사용

```python
import math

print(math.pi) # 3.141592653589793
print(math.ceil(5.1)) # 6 / 올림
```

</div>
</details>

---

<details>
<summary>4일차 학습 요약</summary>
<div>

### 문자형

#### 문자열 생성

```python
str1 = 'Hello Python'
str2 = "Anaconda"
str3 = """이것도 가능해"""
str4 = '''이것도 가능하구나'''

빈 문자열 생성
str_t1 = ''
str_t2 = str()
```

#### 이스케이프 문자

- \n : 개행
- \t : 탭
- \\ : 문자
- \' : 문자
- \" : 문자
- \000 : 널 문자

```python
print("I'm Boy") # I'm boy
print('I\'m boy') # I'm boy
print('a \t b') # a        b
print('a \n b') #a
                # b
```

#### 멀티라인 입력

- ''' ''' 또는 """ """
- \ 를 사용하면 개행할 수 있다

```python
multi_str = '''
멀티라인을
입력해볼게요
과연 이게 문자열인가요?
'''

multi_str2 = \
'''
역 슬래시(\)를 사용하면
개행을 할 수 있다
개행한 다음의 내용이 변수에 할당된다.
'''
```

#### 문자열 연산

```python
### 시퀀스는 'in' 과 'not in' 연산을 지원한다.
str_o1 = 'Hello'
str_o2 = 'Python'
str_o3 = 'How are you?'

print ('a' not in str_o1) # True
print('p' in str_o2) # False
print('P' in str_o2) # True
print('?' in str_o3) # True
```

#### 문자열 형 변환

- <code>str()</code> : 문자형으로 변환

```python
is_str1 = str(123)
is_str2 = str(True)
is_str3 = str(3.14)
print (type(is_str1)) # <class 'str'>
print (type(is_str2)) # <class 'str'>
print (type(is_str3)) # <class 'str'>
```

#### 문자열 함수

- <code>len(str)</code> : 문자열 길이 확인
- <code>upper()</code> : 대문자로 변환
- <code>capitalize()</code> : 첫번째 문자를 대문자로 변환
- <code>isalpha()</code> : 문자만 있는지 확인
- <code>isalnum()</code> : 문자와 숫자만 있는지 확인
- <code>startswith()</code> : 문자열의 시작이 무엇인지 확인
- <code>endwith()</code> : 문자열의 끝이 무엇인지 확인
- <code>count()</code> : 문자열에 몇 개의 문자가 있는지 확인
- <code>replace(old, new)</code> : old -> new 문자열을 변경한다.
- <code>split()</code> : 문자열을 구분자로 나누어 리스트로 반환한다.
- <code>sorted()</code>: 문자열을 정렬한다. (a-z 순서대로)

#### 반복(시퀀스)

- <code>dir()</code> : 객체에 정의된 변수 또는 함수를 보여준다. \_\_iter\_\_가 있다면 반복(시퀀스) 가능

```python
im_str = 'Good Boy!'

print(dir(im_str))
for i in im_str:
    print(i)
```

#### 슬라이싱

```python
str_s1 = "Hello Python"

print(str_s1[4]) # o
print(str_s1[-1]) # n
print(str_s1[-3]) # h, 뒤에서 세번째
print(str_s1[0:3]) # Hel, 0~3
print(str_s1[:3]) # Hel, 처음~3
print(str_s1[3:]) # lo Python, 3~마지막
print(str_s1[:len(str_s1)]) # Hello Python, 처음~문자길이
print(str_s1[:len(str_s1) - 1]) # Hello Pytho, 처음~(문자 길이 + 연산)
print(str_s1[1:9:3]) # eoy, 3번째는 간격, 처음~9 3번씩 건너뛴 문자열
print(str_s1[-5:]) # ython, 뒤에서 5~마지막
print(str_s1[1:-2]) # ello Pyth, 1~마지막에서 두번째 전까지
print(str_s1[::2]) # HloPto, 처음~마지막 2개씩 건너뛴 문자열
print(str_s1[::-1]) # nohtyP olleH, 역순
```

#### 아스키 코드(ASCII)

- <code>ord()</code> : 문자 -> 아스키 코드
- <code>chr()</code> : 아스키 코드 -> 문자

```python
ord('z') # 122
chr(122) # 'z'
```

</div>
</details>

---

<details>
<summary>5일차 학습 요약</summary>
<div>

### 리스트 자료형 - 1

#### 리스트

- 순서가 있다. (반복이 가능하다)
- 중복이 허용된다.
- 수정 및 삭제가 가능하다.

#### 선언

```python
a = [] # <class 'list'>
b = list()
c = [5, 10 ,15]
d = [1000, 10000, 'Ace', 'Base', 'Captain']
e = [1, 10, 100, ['january', 'february', 'march']]
f = [21.42, 'footbar', 3, 4, False, 3.14159]
```

#### 인덱싱

```python
print('d : ', type(d), d) # d :  <class 'list'> [1000, 10000, 'Ace', 'Base', 'Captain']
print('d[1] : ', d[1]) # 10000
print('연산도 가능 : ', d[0] + d[1]) # 11000
print('배열 내 배열에 접근 : ', e[-1][1]) # february
print('문자를 배열로 변환 : ', list(e[-1][1])) # ['f', 'e', 'b', 'r', 'e', 'b', 'l', 'y']
```

#### 슬라이싱

```python
print('d[1:3] : ', d[0:3]) # [1000, 10000, 'Ace']
print(d[2:]) # ['Ace', 'Base', 'Captain']
print(e[-1][1:3]) # ['february', 'march']
```

#### 리스트 연산

```python
print(c + d) # [5, 10, 15, 1000, 10000, 'Ace', 'Base', 'Captain']
print(d + c) # [1000, 10000, 'Ace', 'Base', 'Captain', 5, 10, 15]
print(c * 3) # [5, 10, 15, 5, 10, 15, 5, 10, 15]
```

</div>
</details>

---

<details>
<summary>6일차 학습 요약</summary>
<div>

### 리스트 자료형 2

#### 리스트 비교

```python
c = [1,2,3,4,5,6]
## 값 비교
print(c == c[:3] + c[3:]) # True

## 같은 id 값
temp = c
print(c == temp) # True
print(id(c) == id(temp)) # True, 파이썬은 내부적으로 최적화를 해서 자료구조를 저장하고 있다.
```

#### 리스트 수정 삭제

```python
z = [1,2,3,4,5,6]
z[0] = 'a'
print(z) # ['a', 2, 3, 4, 5, 6]
z[1:2] = ['a','b','c']
print(z) # ['a', 'a', 'b', 'c', 3, 4, 5, 6]
z[1:3] = []
print(z) # ['a', 'c', 3, 4, 5, 6]
del z[3]
print(z) # ['a', 'c', 3, 5, 6]
```

#### 리스트 함수(메서드)

- <code>myList.append(1)</code> : 마지막에 추가
- <code>myList.pop()</code> : 마지막 요소 삭제
- <code>myList.sort()</code> : 오름차순 정렬
- <code>myList.reverse()</code> : 내림차순 정렬
- <code>myList.insert(index, value)</code> : index 위치에 value 추가
- <code>myList.remove(value)</code> : value 삭제
- <code>myList.index(value)</code> : value 위치 확인
- <code>myList.count(value)</code> : value 개수 확인
- <code>myList.clear()</code> : 모든 요소 삭제
- <code>myList.copy()</code> : 복사
- <code>myList.extend(list)</code> : 리스트 연결

```python
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
```

</div>
</details>

---
