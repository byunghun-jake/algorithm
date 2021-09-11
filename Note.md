### 진수 변환

#### 나머지, 몫 활용

```python
def decimal_to_binary(decimal_num):
    binary_num = ""
    while decimal_num:
        binary_num = str(decimal_num % 2) + binary_num
        decimal_num //= 2
    return binary_num
```



#### 진수 변환 메서드 활용

```python
# 10진수 => 2진수
bin(decimal_num)

# 10진수 => 8진수
oct(decimal_num)

# 10진수 => 16진수
hex(decimal_num)
```



#### ⭐ format 활용

```python
def decimal_to_binary(decimal_num):
    return f"{decimal_num:b}"

def decimal_to_oct(decimal_num):
    return f"{decimal_num:o}"

def decimal_to_hex(decimal_num):
    return f"{decimal_num:x}"

# 변환 시 생성되는 이진수가 10자리로 통일되도록 하려면?
def decimal_to_binary(decimal_num):
    return f"{decimal_num:010b}"
```



### Transpose

#### 인덱스 접근

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def transpose(m):
    N = len(m)
    m_t = []
    for c in range(N):
        t_row = []
        for r in range(N):
            t_row.append(m[r][c])
        m_t.append(t_row)
    return m_t

t_matrix = transpose(matrix)
```



#### ⭐ zip 메서드 사용

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

t_matrix = list(map(list, zip(*matrix)))
```



### List 순환

#### ⭐enumerate

```python
names = ["죠르디", "라이언", "콘"]
ages = [3, 7, 7]

for idx, value in enumerate(zip(names, ages)):
    print(idx, value)
  	# 1 ("죠르디", 3)
    # 2 ("라이언", 7)
    # 3 ("콘", 7)
```



### 정렬(Sort)

#### 정렬 기준이 2개 이상일 때,

```python
numbers = [30, 1, 29, 4]
scores = [100, 90, 80, 80]

# 점수 내림차순
# 점수가 동일할 때 번호 오름차순
students = list(zip(numbers, scores))
students.sort(key=student: (-student[1], student[0]))
```



### 집합(Set)

```python
# 중복 제거
arr1 = [1, 1, 2, 2, 3, 4, 5, 6, 6, 6]
unique_arr1 = list(set(arr1))
# [1, 2, 3, 4, 5, 6]

# 두 집합에서 겹치는 요소 제거 (차집합)
arr2 = [1, 3, 5, 7, 9]
arr1_minus_arr2 = list(set(arr1) - set(arr2))
# [2, 4, 6]
```



### 소수 구하기

#### 반복문

1과 자신 외에 다른 수로 나누어떨어지는 수

반복하는 범위가 중요하다.

1. 모든 범위: `range(2, N)`
2. 제곱근까지의 범위: `range(2, int(N ** 0.5) + 1)`

```python
def check_prime_num(num):
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False
	return True
```



### 조합 구하기

#### 반복문

```python
nums = [1, 2, 3, 4]
length = 2
combs = []

def get_combination(temp, s):
    if len(temp) == length:
        combs.append(temp)
        return
    for idx in range(s, len(nums)):
        # temp에 추가하고 다음으로 넘어가는 경우
        get_combination(temp + [nums[idx]], idx + 1)

get_combination([], 0)
```



#### ⭐combinations

```python
from itertools import combinations as cb

nums = [1, 2, 3, 4]
combs = list(cb(nums, 2))
# [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
```

