# Today I Learned

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
