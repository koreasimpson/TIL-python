# Today I Learned

<details>
<summary>template</summary>
<div>

### 제목

#### 부제목1

- 부제목 내용

```
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

```
    print("P", "Y", "T", "H", "O", "N", sep='')
    // PYTHON
    print("P", "Y", "T", "H", "O", "N", sep='-')
    // P-Y-T-H-O-N
```

#### End 사용

- print 내용간 줄바꿈이 되어 출력되지 않고, end 옵션의 내용 다음에 같은 라인에서 출력된다.

```
    print('Welcome to', end='')
    print(' Python', end='     last')
    print('!')
    // Welcome to Python     last!
```

#### Python Format 사용

- format 옵션(d, s, f, ...) // d: digit, s: string, f: float, ...
- format 옵션을 사용하면 출력되는 문자열을 자동으로 포맷팅하여 출력한다.

```
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

```
num1 = 100
str1 = 'Hello'
```

#### 자료형

- <code>type(n)</code> : 변수의 자료형을 확인

```
num1 = 700
str1 = 'Hello'

print(type(num1)) # <class 'int'>
print(type(num1)) # <class 'str'>
```

#### 값 복사

- 파이썬에서는 값 참조가 아닌 값 복사가 된다.

```
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

```
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
