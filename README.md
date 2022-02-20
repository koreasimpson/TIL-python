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

- <code>type(n)</code>변수의 자료형을 확인

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

- <code>id(변수)</code> 객체의 고유값 확인
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
