### 최솟값 만들기

#### 핵심 포인트

- 두 배열의 각 요소를 곱해, 최소값을 만들자



#### 내 코드

- `sort()`
- `zip()`

```python
# 곱을 최소로 만들려면?
# 한 배열은 오름차순
# 한 배열은 내림차순
# 큰 값과 작은 값을 곱하는 방식으로 누적하면 되지 않을까?

def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for n, m in zip(A, B):
        answer += n * m
    return answer
```



### 최댓값과 최솟값

#### 핵심 포인트

- 문자열을 배열로 변환할 수 있는가?
- 배열 요소를 형변환할 수 있는가?

#### 내 코드

- `map()`
- `join()`

```python
# 공백으로 구분되어 있는 문자를 배열로 변환시킨다.
# 배열에 있는 값을 int형으로 변환한다.
# 배열에 있는 값을 오름차순으로 정렬한다.
# 첫 번째 값과 마지막 값을 저장한다.
# 요소를 str형으로 변환한다.
# 문자열로 합친 뒤 리턴한다.

def solution(s):
    answer = ''
    num_list = list(map(int, s.split()))
    num_list.sort()
    answer_list = list(map(str, [num_list[0], num_list[-1]]))
    answer = " ".join(answer_list)
    return answer
```



#### 다른 사람 코드

- `max()`, `min()`

```python
def solution(s):
    num_list = list(map(int, s.split()))
    return f"{min(num_list)} {max(num_list)}"
```



### 숫자의 표현

#### 핵심 포인트

- 윈도우 슬라이드? 문제?



#### 내 코드

```python
# 1부터 더해가며 누적합을 구한다.
# 값이 일치하면, answer++
# 값이 지정한 값보다 크면, 값이 일치하거나 작아질 때까지 pop(0)
# 값이 일치하면, answer++
# 값이 작으면 반복
def solution(n):
    # n 자기 자신일 때
    answer = 1
    i = 0
    arr = []
    while i < n:
        if sum(arr) == n:
            print(arr, i)
            answer += 1
            arr.append(i)
            i += 1
        elif sum(arr) < n:
            arr.append(i)
            i += 1
        else:
            arr.pop(0)
    return answer
```



### ❌ 땅따먹기

#### 오답

```python
# 한 행에서 최대 값 2개만 알고 있으면 되는 문제 아닐까?

# 1. 모든 경우의 수를 다 고려해보자
    # 1. 현재 행에서 0번부터 N - 1까지 열을 선택하고, 다음 행으로 넘어간다 (선택한 열, 누적 합을 넘겨준다).
        # 1-1. 현재 행에서 0 ~ N-1 중 이전 행에서 선택한 행을 제외한 행을 선택하고 다음 행으로 넘어간다.(반복)
import sys

sys.setrecursionlimit(1000001)
        
max_score = 0

def solution(land):
    answer = 0
    N = len(land)
    
    def ddang(cr, bc, total_score):
        global max_score
        if cr == N:
            max_score = max(total_score, max_score)
            return
        for cc in range(4):
            if cc == bc:
                continue
            ddang(cr + 1, cc, total_score + land[cr][cc])
    ddang(0, 5, 0)
    answer = max_score    
    
    
    return answer
```



#### 핵심 포인트

- Dynamic Programming

  작게 나누어 생각하기



#### 내 코드

```python
def solution(land):
    answer = 0
    N = len(land)
    for r in range(1, N):
        land[r][0] = land[r][0] + max([land[r - 1][1], land[r - 1][2], land[r - 1][3]])
        land[r][1] = land[r][1] + max([land[r - 1][0], land[r - 1][2], land[r - 1][3]])
        land[r][2] = land[r][2] + max([land[r - 1][0], land[r - 1][1], land[r - 1][3]])
        land[r][3] = land[r][3] + max([land[r - 1][0], land[r - 1][1], land[r - 1][2]])
    answer = max(land[N - 1])
    return answer
```



#### 다른 사람 코드

```python
def solution(land):

    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] = max(land[i -1][: j] + land[i - 1][j + 1:]) + land[i][j]

    return max(land[-1])
```

