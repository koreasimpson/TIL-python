# Chapter02 : 파이썬 완전 기초
# Chapter02-01 : print 사용법
# 참조 : https://www.python-course.eu/python3_formatted_output.php

print('Python Start!')
print("Python Start!")
print('''Python Start!''')
print("""Python Start!""")
print('')

# separator 옵션
# sep='' sep에 할당된 값이 각각의 문자 사이에 들어간다. 예제 케이스는 공백이 없음
print("P", "Y", "T", "H", "O", "N", sep='')
print("P", "Y", "T", "H", "O", "N", sep='-')
print('')

# end 옵션
# print 내용간 줄바꿈이 되어 출력되지 않고, end 옵션의 내용 다음에 같은 라인에서 출력된다.
print('Welcome to', end='')
print(' Python', end='     last')
print('!')
print('')


# file 옵션
import sys
print('Learn Python', file=sys.stdout)
print('')

# format 옵션(d, s, f, ...) // d: digit, s: string, f: float, ...
# format 옵션을 사용하면 출력되는 문자열을 자동으로 포맷팅하여 출력한다.
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))
print('')

# %s
print('%10s' % ('welcome')) # 10자리 확보
print('{:>10}'.format('welcome')) # 오른쪽 정렬

print('%-10s' % ('welcome')) # 총 10자리로 출력 & 왼쪽 정렬
print('{:<10}'.format('welcome')) # 총 10자리로 출력 & 왼쪽 정렬

print('{:_>10}'.format('welcome')) # 총 10자리로 출력 & 오른쪽 정렬 & 공백 채우기
print('{:^10}'.format('welcome')) # 총 10자리로 출력 & 가운데 정렬

print('%5s' % ('welcome to python')) # 모든 텍스트 출력
print('%.5s' % ('welcome to python')) # 최대 5자리까지만 출력
print('{:10.5}'.format('welcome to python')) # 공간 10자리 확보 & 최대 5자리까지만 출력
print('')

# %d
print('%d %d' % (1, 2))
print('{} {}'.format(1, 2))

print('%4d' % (42)) # 4자리 확보
print('{:4d}'.format(42)) # 4자리 확보

# %f
print('%f' % (3.141592653589793))
print('%1.2f' % (3.141592653589793)) # 정수, 소수 자리수 지정
print('{:f}'.format(3.141592653589793)) # 정수, 소수 자리수 지정
print('{:06.2f}'.format(3.141592653589793)) # 정수, 소수 자리수 지정