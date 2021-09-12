### 백준 - 5430 (AC)

[큐덱 - AC](https://www.acmicpc.net/problem/5430)

#### 내 코드 (성능 🤣)

```python
import sys

TC = int(sys.stdin.readline().strip())

for tc in range(TC):
    operations = sys.stdin.readline().strip()
    N = int(sys.stdin.readline().strip())
    NUMS = sys.stdin.readline().strip()[1:-1]
    direction = True
    if len(NUMS) < 1:
        num_list = []
    else:
        num_list = list(map(int, NUMS.split(",")))
    for operation in operations:
        if operation == "R":
            direction = not direction
        elif operation == "D":
            if len(num_list) < 1:
                print("error")
                break
            if direction:
                num_list.pop(0)
            else:
                num_list.pop()
    else:
        if not direction:
            num_list = num_list[::-1]
        print(f"[{','.join(list(map(str, num_list)))}]")
```



#### 다른 분 코드 참고 (성능 😍)

```python
for tc in range(TC):
    operations = sys.stdin.readline().strip()
    N = int(sys.stdin.readline().strip())
    NUMS = sys.stdin.readline().strip()[1:-1].split(",")
    is_front_pop = True
    start_idx = 0
    end_idx = N
    for operation in operations:
        if operation == "R":
            is_front_pop = not is_front_pop
        else:
            if end_idx <= start_idx:
                print("error")
                break
            if is_front_pop:
                start_idx += 1
            else:
                end_idx -= 1
    else:
        answer = NUMS[start_idx:end_idx]
        if not is_front_pop:
            answer = answer[::-1]

        print(f"[{','.join(answer)}]")
```



**성능 차이**

> Why?
>
> 내가 처음에 짠 코드는 매번 배열의 길이에 변화를 주는, 특히 pop(0)과 같이 시간이 오래걸리는 연산을 했기 때문이다.
>
> 배열의 양쪽 끝에 변화가 생긴다면, 양 끝 인덱스를 조작하는 것으로 대체할 수 있다는 생각을 해야겠다.

![image-20210707192813558](README.assets/image-20210707192813558.png)





### 백준 - 2630 (색종이 만들기)

[링크](https://www.acmicpc.net/problem/2630)

#### 이론

- 쿼드트리





#### 내 코드

```python
# 2중 반복문을 
def check_board_color(r, c, n):
    color = BOARD[r][c]
    for i in range(r, r + n):
        for j in range(c, c + n):
            if color != BOARD[i][j]:
                return False
    return True


def solve(r, c, n):
    # board 탐색
    if check_board_color(r, c, n):
        # 해당하는 색 카운팅
        color = BOARD[r][c]
        paper_count[color] += 1
    else:
        # 4개로 분할한 뒤 재귀호출
        mid = n // 2
        # 2사분면
        solve(r, c, mid)
        # 1사분면
        solve(r + mid, c, mid)
        # 3사분면
        solve(r, c + mid, mid)
        # 4사분면
        solve(r + mid, c + mid, mid)


N = int(input())
BOARD = [list(map(int, input().split())) for _ in range(N)]
paper_count = [0, 0]

solve(0, 0, N)
print(paper_count[0])
print(paper_count[1])
```



### 백준 2667 단지번호붙이기



#### 내 코드

```python
# 1. 1의 값을 찾는 과정
# 2. 1을 찾았을 때, 해당 지점을 방문한 적이 있었는지 확인
# 3. 방문한 적이 있었다면 넘어간다.
# 4. 방문한 적이 없었다면 그 위치를 기준으로 4방향으로 탐색을 진행한다.
# 5. 탐색이 끝났다면 단지의 크기를 저장한다.
# 6. 단지 인덱스를 1 크게 해준 뒤, 다시 1번으로 돌아간다.

# N: 지도의 크기 (~25)
N = int(input())
MAP = [list(map(int, list(input()))) for _ in range(N)]
visited = [[False] * N for _ in range(N)]


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(sr, sc):
    count = 1
    queue = [(sr, sc)]
    visited[sr][sc] = True

    while queue:
        snr, snc = queue[0]
        for i in range(4):
            nnr = snr + dr[i]
            nnc = snc + dc[i]
            if 0 <= nnr < N and 0 <= nnc < N:
                if MAP[nnr][nnc] and not visited[nnr][nnc]:
                    queue.append((nnr, nnc))
                    count += 1
                    visited[nnr][nnc] = True
        else:
            queue.pop(0)
    return count


count_list = []

for r in range(N):
    for c in range(N):
        if MAP[r][c] and not visited[r][c]:
            count_list.append(bfs(r, c))

print(len(count_list))
for count in sorted(count_list):
    print(count)
```





#### 다른 사람 코드

- 인덱스 범위를 넘어가는 지 확인하는 부분에서 `ny in range(N)`과 같이 `in` 연산자와 `range()`를 사용했다.

- BFS를 구현하기 위해 deque를 사용했다.

  `queue.pop(0) === dq.popleft()`

```python
from collections import deque

N = int(input())
map_arr = [list(input()) for _ in range(N)]

def bfs(y, x, cnt):
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]
    dq = deque([(y, x)])
    while dq:
        y, x = dq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny in range(N) and nx in range(N) and map_arr[ny][nx] == '1':
                map_arr[ny][nx] = '0'
                dq.append((ny, nx))
                cnt += 1
    return cnt

answer = []
for y in range(N):
    for x in range(N):
        if map_arr[y][x] == '1':
            map_arr[y][x] = '0'
            result = bfs(y, x, 1)
            answer.append(result)

print(len(answer))
for i in sorted(answer):
    print(i)
```





### 1012_유기농 배추

```python
# 지렁이의 이동 범위는 기준 위치에서 상하좌우
# 배추를 지키기 위해 필요한 최소 지렁이의 마리수를 구해라
# 배추 군집의 개수를 구하면 된다.

import sys
from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(sr, sc):
    dq = deque([(sr, sc)])
    visited[sr][sc] = 1

    while dq:
        cr, cc = dq.popleft()

        for di in range(4):
            nr = cr + dr[di]
            nc = cc + dc[di]
            if nr in range(N) and nc in range(M):
                if MAP[nr][nc] and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    dq.append((nr, nc))


# T: 테스트 케이스
T = int(input())

for tc in range(T):
    # M: 가로 길이 (~50)
    # N: 세로 길이 (~50)
    # K: 배추의 개수 (~2500)
    M, N, K = map(int, input().split())

    answer = 0

    MAP = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    for _ in range(K):
        c, r = map(int, sys.stdin.readline().strip().split())
        MAP[r][c] = 1

    for r in range(N):
        for c in range(M):
            if MAP[r][c] and not visited[r][c]:
                bfs(r, c)
                answer += 1

    print(answer)
```



#### 다른 사람 코드

- 재귀로 넘겨줄 때, 인자를 바꿔서 보내주는 방식이 인상적

```python
import sys
sys.setrecursionlimit(3000)

def dfs(i, j, N, M, np):
    if i < 0 or j >= N or i >= M or j < 0 or np[i][j] == 0: return
    np[i][j] = 0
    dfs(i + 1, j, N, M, np)
    dfs(i, j + 1, N, M, np)
    dfs(i - 1, j, N, M, np)
    dfs(i, j - 1, N, M, np)

T = int(sys.stdin.readline())
for i in range(T):
    N, M, K = map(int, sys.stdin.readline().split()); earthworm = 0
    Napa = [[0] * N for _ in range(M)]
    for j in range(K):
        x, y = map(int, sys.stdin.readline().split())
        Napa[y][x] = True
    for x in range(M):
        for y in range(N):
            if Napa[x][y] == True:
                dfs(x,y,N,M,Napa); earthworm += 1
    print(earthworm)
```





### 2178_미로탐색



### 7576_토마토

#### 내 코드 - 2

- 모든 행/열을 탐색하는 것은 비효율적이라고 생각
- 처음 행/열을 탐색할 때, 익지 않은 토마토의 개수를 따로 저장하여 bfs 탐색 시 상태가 변화하였을 때 1씩 차감하여 남은 토마토의 개수를 확인할 수 있을 것





#### 내 코드 - 1

- 모든 행, 열을 탐색하여 익은 토마토의 위치를 저장
- 익은 토마토의 위치를 가지고 bfs 탐색
- 방문기록을 남기는 대신 익지 않은 토마토에서 익은 토마토로 값을 직접 변경 (0 => 1)

- 탐색이 종료된 뒤, 모든 행/열을 탐색하여 안익은 토마토가 있는지 확인

```python
from collections import deque


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs():
    result = 0
    while dq:
        cr, cc, day = dq.popleft()
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if nr in range(R) and nc in range(C) and MAP[nr][nc] == 0:
                dq.append((nr, nc, day + 1))
                MAP[nr][nc] = 1
                result = day + 1

    return result



C, R = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(R)]
# 직접 값을 바꿔보자

dq = deque([])

for r in range(R):
    for c in range(C):
        if MAP[r][c] == 1:
            dq.append((r, c, 0))

answer = bfs()

for r in range(R):
    for c in range(C):
        if MAP[r][c] == 0:
            answer = -1

print(answer)
```



### 7562_나이트의 이동

> 유효성 검사를 할 때, `range`를 사용하는 경우 시간초과가 발생하는 케이스

#### 하이라이트

```python
if 0 <= nr < L and 0 <= nc < L and not visited[nr][nc]:
	# 통과

if nr in range(L) and nc in range(L) and not visited[nr][nc]:
    # 시간초과
```



#### 내 코드

```python
# BFS
# 1. 8개 방향으로 이동
# 2. 방문 기록
# 3. queue 에 저장
# 몇 번만에 이동했는지 출력해야 한다.
from collections import deque

dr = [-2, -1, 1, 2, 2, 1, -1, -2]
dc = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(r, c):
    global er, ec
    dq = deque([(r, c, 0)])
    visited[r][c] = True

    while dq:
        cr, cc, count = dq.popleft()
        # 도착했는지 확인
        if cr == er and cc == ec:
            return count

        # 8개 방향 탐색
        for i in range(8):
            nr = cr + dr[i]
            nc = cc + dc[i]
            # range는 시간이 많이 걸린다.
            # if nr in range(L) and nc in range(L) and not visited[nr][nc]:
            if 0 <= nr < L and 0 <= nc < L and not visited[nr][nc]:
                if cr == er and cc == ec:
                    return count
                dq.append((nr, nc, count + 1))
                visited[nr][nc] = True


TC = int(input())
for tc in range(TC):
    L = int(input())
    sr, sc = list(map(int, input().split()))
    er, ec = map(int, input().split())
    visited = [[False] * L for _ in range(L)]
    answer = bfs(sr, sc)
    print(answer)
```



### 1707_이분그래프

#### 하이라이트

- 이분그래프란?

  > 인접한 노드 끼리 같은 그룹에 해당하지 않는 그래프

  ![img](https://media.vlpt.us/images/i-zro/post/2e66bcb7-05f8-45e0-a794-a272eb508d06/image.png)

- 메모리초과 발생

  N1과 N2가 연결되어 있을 때, `board[N1][N2] = board[N2][N1] = True`와 같이 저장하였더니 메모리를 초과해버렸다.

  이차원 배열을 만들었기 때문에 생긴 일 같은데, 배열의 크기는 다음과 같다.

  `V(1 <= V <= 20,000)`

  2만개 이상 넘어가는 경우에는 메모리초과에 주의해야겠다.

  ---

  해결책:

  `[[], [], [], ...]`1차원 배열을 만들어, 해당하는 index에 연결된 노드 번호를 추가해주는 방식으로 진행했다.

  

- 시간초과 발생

  어디에서 시간을 줄여야 할까?

  - 다음 그룹을 지정할 때, 나머지 연산을 수행하는 데, 여기에서 시간이 오래 걸리는 걸까?

    그룹을 -1과 1로 나누어 배정하는 것으로 변경해보자.

    > 해결하지 못했다.

  - 갈 수 있는지 확인하는 부분을 다르게 생각해보자.

    n1 이라는 노드에서 모든 노드를 탐색하며 갈 수 있는지 없는지 확인하는 것 보단, 앞서 저장해 두었던, 연결된 노드를 저장한 리스트를 활용하는 것이 효율적일 것이라는 생각이 든다.

    ```python
    # 이전
    for nn in range(1, node_count + 1):
        if nn not in board[cn]:
            continue
    ```

    ```python
    # 이후
    for nn in board[cn]:
    ```

  

- 틀렸습니다

  아예 연결이 끊긴 노드가 있을 수 있다는 것을 고려하지 않았다.

  모든 노드를 시작점으로 탐색을 수행해야 하며, 만일 1이 아닌 노드에서 다시 탐색을 수행할 수 있다면 그 그래프는 이분탐색 그래프일 수 없을 것

  ```python
  # 이전
  bfs(1)
  ```

  ```python
  # 이후
  for sn in range(1, node_count + 1):
      if not visited[sn]:
          answer = bfs(sn)
          if answer == "NO":
              break
  ```

  

#### 내 코드 - 정답

```python
# 인접한 정점들과는 다른 그룹에 속하는지 확인
import sys
from collections import deque


def bfs(sn):
    dq = deque([sn])
    visited[sn] = 1

    while dq:
        cn = dq.popleft()
        for nn in board[cn]:
            # 그룹 확인
            if visited[nn] == 0:
                dq.append(nn)
                visited[nn] = -visited[cn]
            elif visited[nn] == visited[cn]:
                return "NO"
    return "YES"



TC = int(input())
for tc in range(TC):
    node_count, line_count = map(int, input().split())
    board = [[] for _ in range(node_count + 1)]
    visited = [0] * (node_count + 1)

    for _ in range(line_count):
        r, c = map(int, sys.stdin.readline().strip().split())
        board[r].append(c)
        board[c].append(r)

    answer = ""
    for sn in range(1, node_count + 1):
        if not visited[sn]:
            answer = bfs(sn)
            if answer == "NO":
                break
    print(answer)
```





#### 내 코드 - 시간초과

```python
# 인접한 정점들과는 다른 그룹에 속하는지 확인
import sys
from collections import deque


def bfs(sn):
    dq = deque([(sn, 1)])
    group[sn] = 1

    while dq:
        cn, t = dq.popleft()
        for nn in range(1, node_count + 1):
            # 갈 수 있는지 확인
            if nn not in board[cn]:
                continue
            # 그룹 확인
            if group[nn] == 0:
                dq.append((nn, t * (-1)))
                group[nn] = t * (-1)
            elif group[nn] == t:
                return "NO"
    return "YES"



TC = int(input())
for tc in range(TC):
    node_count, line_count = map(int, input().split())
    board = [[] for _ in range(node_count + 1)]
    group = [0] * (node_count + 1)

    for _ in range(line_count):
        r, c = map(int, sys.stdin.readline().strip().split())
        board[r].append(c)
        board[c].append(r)

    print(bfs(1))
```







#### 현재 코드

```python
import sys

sys.stdin = open("1210_Ladder1.txt")
# 어느 사다리를 고르면 X표시에 도착하게 될까?

# X 표시에서 거꾸로 올라가는 것으로 전환해보자
# 가로선을 만났을 떄 어떻게 동작해야 할까?
    # 위로 올라가던 중 좌 or 우에 있는 가로선을 만나면, 그 가로선으로 이동한다.
    # 현재 위치에서 좌, 우를 탐색한 뒤
        # 있으면 해당 가로선으로 이동
        # 없으면 위 칸으로 이동
    
    # 좌 or 우로 이동하던 중 위로 갈 수 있는 길을 만나면, 위로 올라간다.

N = 100

for _ in range(1, 11):
    tc = int(input())
    ladder_map = []
    for _ in range(N):
        row = list(map(int, sys.stdin.readline().strip().split()))
        ladder_map.append(row)

    # X 위치를 찾는다.
    start_col = 0
    for idx in range(N):
        if ladder_map[N - 1][idx] == 2:
            start_col = idx
            break

    # X 위치를 시작지점으로 탐색을 시작한다.
    cr = N - 1
    cc = start_col
    c_direction = 0

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    while cr != 0:
        # 좌
        if cc > 1 and ladder_map[cr][cc - 1] == 1:
            while cc > 0 and ladder_map[cr][cc - 1] == 1:
                cc -= 1
            else:
                cr -= 1
                continue
        # 우
        if cc < 99 and ladder_map[cr][cc + 1] == 1:
            while cc < 99 and ladder_map[cr][cc + 1] == 1:
                cc += 1
            else:
                cr -= 1
                continue
        # 양쪽 다 없을 때
        cr -= 1
        cc = cc
    print(f"#{tc} {cc}")
```





#### 과거 코드

```python
N = 100

for _ in range(10):
    # 1. test_case 번호 입력
    tc = int(input())

    # 2. 100x100 배열 입력
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    # 3. [99, 0] 부터 오른쪽으로 이동하며, 2의 위치 찾기
    r = N - 1
    c = 0
    for c_idx in range(N):
        if arr[r][c_idx] == 2:
            c = c_idx
            break
    
    # 4. 도착점부터 위로 올라가며, 작업 수행
    while r > 0:
        # 4-1. 좌우를 탐색하며 1을 찾는다.
        dc = 0
        nc = 0

        # 왼쪽 확인
        if 0 <= c-1 and arr[r][c-1] == 1:
            dc = -1
        elif c+1 < 100 and arr[r][c+1] == 1:
            dc = 1

        if dc:
            nc = c + dc
            while 0 <= nc < 100 and arr[r][nc] == 1:
                nc += dc
            else:
                nc -= dc
                c = nc
        r -= 1
        if r == 0:
            break
    result = c

    print(f"#{tc} {result}")
```



### 1211. Ladder2

- 시작지점의 column 리스트를 저장한다.
- 각 시작지점 별로 탐색을 진행하고, 최소값과 최소값을 갖게 하는 시작 column 위치를 업데이트한다.

```python
# 출발점에서 도착점까지의 거리 구하기

import sys

sys.stdin = open("Ladder2.txt")


N = 100
for _ in range(10):
    tc = int(input())
    ladder = []
    cc_list = []

    for idx in range(N):
        ladder.append(list(map(int, input().split())))
        if idx == 0:
            for c in range(N):
                if ladder[idx][c] == 1:
                    cc_list.append(c)


    min_count = 987654321
    answer = 0
    for idx in range(len(cc_list)):
        cc = cc_list[idx]
        cr = 0
        count = 0
        while cr != 99:
            dc = 0
            if cc > 0 and ladder[cr][cc - 1] == 1:
                dc = -1
            elif cc < 99 and ladder[cr][cc + 1] == 1:
                dc = 1

            if dc:
                while 0 <= cc + dc <= 99 and ladder[cr][cc + dc] == 1:
                    cc += dc
                    count += 1
            cr += 1
            count += 1
        if count < min_count:
            min_count = count
            answer = cc_list[idx]
    print(f"#{tc} {answer}")
```



### 1244_최대 상금

#### 내 코드

##### 메모리 초과

- 불필요한 중복이 너무 많이 생길 것

```python
T = int(input())


def solve(change):
    global answer

    if change == 0:
        temp_number = int("".join(map(str, number_list)))
        answer = max(answer, temp_number)
        return

    for i in range(len(number_list)):
        for j in range(len(number_list)):
            if i == j:
                continue
            # 두 값을 교환
            number_list[i], number_list[j] = number_list[j], number_list[i]
            solve(change - 1)
            # 원래대로
            number_list[i], number_list[j] = number_list[j], number_list[i]

for tc in range(1, T + 1):
    origin_number, change_count = map(int, input().split())
    number_list = list(map(int, str(origin_number)))

    answer = origin_number
    solve(change_count)
    print(f"#{tc} {answer}")
```



- `0`번째 인덱스 부터 `N-1`번째 인덱스까지 순환 [i]
  - `i + 1`부터 `N - 1`까지 수를 비교하며, `i`번째 값보다 큰 값들 중 가장 큰 값을 찾는다. [`idx`]
  - `i`번째 값과 `idx`번째 값을 교환한다.

##### 오답

- 32888에 대한 답을 88823으로 하였다.

```python
# 두 인덱스에 있는 값을 교환을 했을 때, 교환을 하지 않았을 때로 구분하여 생각

T = int(input())


for tc in range(1, T + 1):
    origin_num, change_count = map(int, input().split())
    num_list = [int(x) for x in str(origin_num)]
    N = len(num_list)

    change = 0
    i = 0
    while change < change_count and i < N:
        idx = i
        num = num_list[i]
        # i + 1번째 인덱스 부터 N - 1번째 인덱스까지의 수 중 i번째 인덱스보다 크면서 가장 큰 수를 찾기
        for j in range(i + 1, N):
            if num <= num_list[j]:
                idx = j
                num = num_list[j]
        # 두 값을 교환
        num_list[i], num_list[idx] = num_list[idx], num_list[i]
        change += 1
        i += 1
    # 교환 횟수가 남아있지 않다면?
    if change == change_count:
        answer = int("".join(map(str, num_list)))
    # 교환 횟수가 남아있다면?
    else:
        # 남은 교환 횟수가 짝수라면, 더이상 교환할 필요가 없다.
        if (change_count - change) % 2 == 0:
            answer = int("".join(map(str, num_list)))
        # 남은 교환 횟수가 홀수라면, 가장 영향이 적도록 만들어주어야 한다.
        else:
            # 중복되는 숫자가 있다면, 그 숫자들끼리 교환하면 되기에 전체 값에는 영향을 주지 않는다.
            duplicated = False
            for i in range(N):
                for j in range(N):
                    if i == j:
                        continue
                    if num_list[i] == num_list[j]:
                        duplicated = True
            if duplicated:
                answer = int("".join(map(str, num_list)))
            else:
                # 영향이 적게 만들어주려면 가장 작은 두 값을 교환한다.
                num_list[-1], num_list[-2] = num_list[-2], num_list[-1]
                answer = int("".join(map(str, num_list)))
    print(answer)

```



# Programmers



## Lv 1

### 비밀지도

#### 핵심 포인트

- 이진수 변환 방법을 아는가?

#### 내 코드

```python
def d_to_b(n, num):
    # n: number(10진수)
    binary_text = format(num, "b")
    l = n - len(binary_text)
    binary_text = "0" * l + binary_text
    return binary_text


def solution(n, arr1, arr2):
    answer = []
    # 숫자 배열을 이진수로 변환한다.
    bi_arr1 = []
    bi_arr2 = []
    for i in range(n):
        # 변환한 이진수를 배열에 저장한다.
        bi_arr1.append(d_to_b(n, arr1[i]))
        bi_arr2.append(d_to_b(n, arr2[i]))
    # 두 배열을 인덱스로 순회하며, 새로운 배열을 만든다.
    for i in range(n):
        temp_row = ""
        for j in range(n):
            # 벽은 "#"으로, 공백(0)은 " "으로 저장한다.
            temp = " "
            # 새로운 배열을 만들 때, 어느 하나라도 벽(1)인 부분이 있다면 벽이다.
            if bi_arr1[i][j] == "1" or bi_arr2[i][j] == "1":
                temp = "#"
            temp_row += temp
        # row 단위로 만들어진 문자열을 저장한다.
        answer.append(temp_row)
    print(arr1, arr2)
    return answer


print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))
```



#### 다른 사람 코드 1

- zip

- format 활용

  `f."{x:016b}"`

```python
def solution(n, *maps):
    return [line(n, a | b) for a, b in zip(*maps)]


def line(n, x):
    return ''.join(' #'[int(i)] for i in f'{x:016b}'[-n:])


def test_sample():
    assert solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]) == [
        '#####',
        '# # #',
        '### #',
        '#  ##',
        '#####',
    ]
    assert solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]) == [
        '######',
        '###  #',
        '##  ##',
        ' #### ',
        ' #####',
        '### # ',
    ]


def test_line():
    assert line(5, 9) == ' #  #'
    assert line(5, 30) == '#### '
    assert line(5, 9 | 30) == '#####'
```





### 상호평가

#### 핵심 포인트

- 주어진 2차원 배열을 Transpose할 수 있는가?

#### 내 코드

```python
def grading(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 50:
        return "D"
    return "F"


def solution(scores):
    answer = ''
    mean_arr = []
    # 자기 자신을 평가한 점수가 자기가 받은 점수 중 유일한 최고점 또는 유일한 최저점일 때 그 점수는 제외한다.
    scores_t = []
    l = len(scores)
    for c in range(l):
        score_list = []
        for r in range(l):
            score_list.append(scores[r][c])
        # 내가 준 점수와 최저점 / 최고점 비교
        min_score = min(score_list)
        max_score = max(score_list)
        score_sum = sum(score_list)
        student_count = l
        if score_list[c] == min_score and score_list.count(min_score) == 1:
            score_sum -= min_score
            student_count -= 1
        elif score_list[c] == max_score and score_list.count(max_score) == 1:
            score_sum -= max_score
            student_count -= 1
        mean_score = score_sum / student_count
        answer += grading(mean_score)

    return answer
```



#### 다른 사람 코드 1

- enumerate
- zip

```python
def get_grade(score):
    if score >= 90 :
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 50:
        return 'D'
    else:
        return 'F'

def solution(scores):
    score_table = list(map(list, zip(*scores)))
    for i, scores in enumerate(score_table):
        min_value, max_value = min(scores), max(scores)
        if scores.count(scores[i]) == 1:
            if scores[i] == min_value or scores[i] == max_value:
                scores.pop(i)
    return ''.join(map(lambda x : get_grade(sum(x) / len(x)), score_table))
```



#### 다른 사람 코드 2

- transpose 방법

```python
def solution(scores) :

    avgs=[]

    score=[ [i[j] for i in scores] for j in range(len(scores))]

    for idx,i in enumerate(score) :

        avg=sum(i) ; length=len(i)

        if i[idx] == max(i) or i[idx] == min(i) :

            if i.count(i[idx]) == 1 :

                avg-=i[idx] ; length-=1

        avgs.append(avg/length)

    return "".join([ avg>=90 and "A" or avg>=80 and "B" or avg>=70 and "C" or avg>=50 and "D" or "F" for avg in avgs ])
```



#### 다른 사람 코드 3

- Counter

```python
from collections import Counter
def solution(scores):   
    answer = ''

    for idx, score in enumerate(list(map(list, zip(*scores)))):
        length = len(score)
        if Counter(score)[score[idx]] == 1 and (max(score) == score[idx] or min(score) == score[idx]):
            del score[idx]
            length -= 1

        grade = sum(score) / length

        if grade >= 90:
            answer += 'A'
        elif grade >= 80:
            answer += 'B'
        elif grade >= 70:
            answer += 'C'
        elif grade >= 50:
            answer += 'D'
        else:
            answer += 'F'

    return answer
```



### 직업군 추천하기

#### 핵심 포인트

- list에서 value를 이용해 index 찾기
- zip 활용

#### 내 코드

- `Array.sort(key=lambda x: (-x[1], x[0]))`
- `value in arr` & `arr.index(value)`

```python
def solution(table, languages, preference):
    answer = ''
    score_list = []
    for i in range(5):
        area_list = table[i].split()
        # 가지고 있는 언어에 따른 점수 계산
        score = 0
        for i in range(len(languages)):
            lan = languages[i]
            # list에 존재하는 지 확인 (index 메서드 에러 방지)
            if lan in area_list:
                score += (6 - area_list.index(lan)) * preference[i]
        score_list.append((area_list[0], score))
    # score_list 정렬
    score_list.sort(key=lambda x: (-x[1], x[0]))
    print(score_list)
    answer = score_list[0][0]
    return answer
```



#### 다른 사람 코드 1

- dictionary로 데이터를 저장하고, get을 통해 가져오는 방식
- zip 함수 사용

```python
def solution(table, languages, preference):
    answer = 'ZZZZZZZZ'
    score_dic = {lang: score for lang, score in zip(languages, preference)}
    max_score = 0
    for row in table:
        r = row.split(' ')
        curr_score = 0
        for i in range(1, len(r)):
            curr_score += score_dic.get(r[i], 0) * (6-i)
        if max_score < curr_score:
            max_score = curr_score
            answer = r[0]
        elif max_score == curr_score and answer > r[0]:
            answer = r[0]


    return answer
```

### 약수의 개수와 덧셈

#### 핵심 포인트

- 제곱수는 약수의 개수가 홀수이다.

#### 내 코드

```python
def solution(left, right):
    answer = 0
    for n in range(left, right + 1):
        count = 0
        start = 1
        end = right + 1
        for r in range(start, end):
            if n % r == 0:
                count += 1
        if count % 2 == 0:
            answer += n
        else:
            answer -= n
    return answer
```

#### 다른 사람 코드

- 제곱수는 약수의 개수가 홀수!

```python
def solution(left, right):
    answer = 0
    for n in range(left, right + 1):
        if int(n ** 0.5) == n ** 0.5:
            answer -= n
        else:
            answer += n
    return answer
```



### 실패율

#### 핵심 포인트

- 배열의 누적합을 떠올릴 수 있는가?

#### 내 코드

```python
def solution(N, stages):
    answer = []
    # 0번째 스테이지는 없다.
    # 1 ~ N + 1까지
    stage_tries = [0] * (N + 2)
    failures = []
    for stage in stages:
        stage_tries[stage] += 1
    
    # i번째 스테이지 총 도전자 수
    i_tries = stage_tries[N + 1]
    for i in range(N, 0, -1):
        i_tries += stage_tries[i]
        fail = 0
        if i_tries != 0:
            fail = stage_tries[i] / i_tries
        failures.append((i, fail))
    
    failures.sort(key=lambda x: (-x[1], x[0]))
    answer = [i[0] for i in failures]
    return answer
```



### 폰켓몬

#### 핵심 포인트

- 가지 수를 하나하나 계산해보지 않는 것

- 내가 구해야 하는 것을 제대로 파악할 것

#### 내 코드

```python
def solution(nums):
    answer = 0
    # set을 이용해 중복을 제거한다
    # set의 길이가 선택하는 가지수(N/2)보다 작다면, set의 길이가 최대가 된다.
    # set의 길이가 선택하는 가지수(N/2)보다 크거나 같다면, N/2가 최대가 된다.
    N = len(nums)
    set_nums = list(set(nums))
    set_length = len(set_nums)
    answer = min(N/2, set_length)
    return answer
```



### 체육복

#### 핵심 포인트

- 주어지는 배열이 정렬이 되어있는지 되어있지 않은지 확인할 것
- set의 차집합을 사용해서, 문제를 더 간단히 할 수 있다.



#### 내 코드

- 한쪽 방향으로 진행해서, 빠지는 친구가 생기지 않도록

```python
def solution(n, lost, reserve):
    answer = 0
    students = [1] * (n + 1)
    for i in lost:
        students[i] -= 1
    for i in reserve:
        students[i] += 1
    
    for i in sorted(reserve):
        if students[i] < 2:
            continue
        if 0 < i - 1 and students[i - 1] == 0:
            students[i] -= 1
            students[i - 1] += 1
        elif i + 1 < n + 1 and students[i + 1] == 0:
            students[i] -= 1
            students[i + 1] += 1
    for i in range(1, n + 1):
        if students[i]:
            answer += 1
    return answer
```

#### 다른 사람의 코드

- set 활용

```python
def solution(n, lost, reserve):
    lost = set(lost)
    num_lost = len(lost)
    reserved = set(reserve) - set(lost)
    losted = set(lost) - set(reserve)

    for r in sorted(reserved):
        if r - 1 in losted:
            losted = losted - {r - 1}

        elif r + 1 in losted:
            losted = losted - {r + 1}

    return n - len(losted)
```



### 모의고사

#### 핵심 포인트

- 패턴을 인지하는 것



#### 내 코드

```python
a_answer = [1, 2, 3, 4, 5] # 5
b_answer = [2, 1, 2, 3, 2, 4, 2, 5] # 8
c_answer = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 10

def solution(answers):
    answer = []
    students = [[1, 0], [2, 0], [3, 0]]
    for i in range(len(answers)):
        ans = answers[i]
        if a_answer[i % 5] == ans:
            students[0][1] += 1
        if b_answer[i % 8] == ans:
            students[1][1] += 1
        if c_answer[i % 10] == ans:
            students[2][1] += 1
    max_score = max([x[1] for x in students])
    answer = [x[0] for x in students if x[1] == max_score]
    return answer
```

#### 다른 사람 코드

- enumerate 사용

```python
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
```



### 키패드 누르기

#### 핵심 포인트

- 키 간 거리를 어떻게 구할 것인가?

#### 내 코드

```python
# 키패드를 2차원 배열로 배치한다.
# [[1, 2, 3], [4, 5, 6], [7, 8, 9], [*, 0, #]]

# 두 번호의 거리는 2차원 배열의 r의 차이 + c의 차이이다.
# [1, 4, 7]은 왼손으로 누른다.
# [3, 6, 9]는 오른손으로 누른다.

# 현재 각 손가락의 위치를 저장하는 배열을 생성한다.
# current_positions: [(3, 0), (3, 2)]
# [왼손 좌표, 오른손 좌표]

# 주어지는 숫자를 확인한다.
# 1. [1, 4, 7] => 왼손
# 2. [3, 6, 9] => 오른손
# 3. [2, 5, 8, 0] => 좌표를 구한다.
    # {2: (0, 1), 5: (1, 1), 8: (2, 1), 0: (3, 1)}
    # 좌표를 기준으로 주어진 숫자와 두 엄지손가락의 거리를 계산한다.
# 어떤 손가락으로 누르는 지 확인한 뒤, 엄지손가락의 위치를 업데이트한다.
# L => current_positions[0] = ??
# R => current_positions[1] = ??

# 종료

keypads = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2),
    0: (3, 1)
}

def solution(numbers, hand):
    answer = ''
    current_positions = [(3, 0), (3, 2)]
    for number in numbers:
        num_pos = keypads[number]
        if num_pos[1] == 0:
            answer += "L"
            current_positions[0] = num_pos
        elif num_pos[1] == 2:
            answer += "R"
            current_positions[1] = num_pos
        else:
            l_diff = abs(current_positions[0][0] - num_pos[0]) + abs(current_positions[0][1] - num_pos[1])
            r_diff = abs(current_positions[1][0] - num_pos[0]) + abs(current_positions[1][1] - num_pos[1])
            if l_diff < r_diff:
                answer += "L"
                current_positions[0] = num_pos
            elif l_diff > r_diff:
                answer += "R"
                current_positions[1] = num_pos
            elif hand == "left":
                answer += "L"
                current_positions[0] = num_pos
            else:
                answer += "R"
                current_positions[1] = num_pos
    return answer
```



### 숫자 문자열과 영단어

#### 핵심 포인트

- replace 메서드를 알고 있는가?

#### 내 코드

- replace 메서드는 체이닝이 가능했다.
- 체이닝이 아닌 다른 방법도 가능하다.

```python
# replace 메서드를 쓰면 될까?
# replace는 여러번 연결시켜서 쓸 수 있을까?

def solution(s):
    answer = 0
    s = s.replace("zero", "0").replace("one", "1").replace("two", "2").replace("three", "3").replace("four", "4").replace("five", "5").replace("six", "6").replace("seven", "7").replace("eight", "8").replace("nine", "9")
    print(s)
    answer = int(s)
    return answer
```

#### 다른 사람 코드

- 변환할 내용을 저장한 뒤, 저장한 내용 전체를 순환하여 replace를 적용하는 방법

```python
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)
```



### 신규 아이디 추천

#### 핵심 포인트

- 너 정규식 쓸 줄 아니?



#### 내 코드 1

- 정규식을 쓰지 않은 버전
- `ord` 이용
- 4번째 단계에서 인덱스 에러 고려

```python
# 1. 정규식을 사용하지 않는 버전
def solution(new_id):
    answer = ''
    # 1. 모든 대문자를 대응되는 소문자로 치환합니다.
    new_id = new_id.lower()
    # 2. 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자 제거
    temp = ""
    for t in new_id:
        if ord("a") <= ord(t) <= ord("z") or ord("0") <= ord(t) <= ord("9") or t in ["-", "_", "."]:
            temp += t
    new_id = temp
    # 3. 마침표가 2번 이상 연속된 부분을 하나의 마침표로 치환
    before_text = ""
    temp = ""
    for t in new_id:
        if before_text == "." and t == before_text:
            continue
        else:
            before_text = t
            temp += t
    new_id = temp
    # 4. 마침표가 처음이나 끝에 위치한다면 제거
    # 문자열을 인덱스로 접근하기 때문에 IndexError 위험
    if len(new_id) > 0 and new_id[0] == ".":
        new_id = new_id[1:]
    if len(new_id) > 0 and new_id[-1] == ".":
        new_id = new_id[:-1]
    # 5. new_id가 빈 문자열이라면, new_id에 "a"를 대입
    if len(new_id) == 0:
        new_id = "a"
    # 6. new_id의 길이가 16자 이상이면, 첫 15자만 남긴다.
    # 줄였을 때, 마지막 문자가 마침표라면 제거한다.
    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id = new_id[:-1]
        
    # 7. new_id의 길이가 2자 이하라면, 길이가 3이 될 때까지 마지막 문자를 더한다.
    while len(new_id) < 3:
        new_id += new_id[-1]
    answer = new_id
    return answer
```



#### 정규표현식 활용

```python
import re
# 1. 패턴에 일치하지 않는 문자 삭제하기(일치하는 문자만 남기기)
new_id = "...!@bat#*..y.abcdefghijklm"
p = re.compile("[a-z0-9-_.]+")
matched_list = re.findall(p, new_id)
# re.findall("[a-z0-9-_.]+", new_id)
# ['...', 'bat', '..y.abcdefghijklm']
new_id = "".join(matched_list)
# ...bat..y.abcdefghijklm


# 2. 문자열 치환
# 마침표가 2개 이상인 경우, 1개로 변환하기
new_id = "...asdf..asdf..."
p = re.compile("[.]{2,}")
new_id = re.sub(p, ".", new_id)
# .asdf.asdf.

# 마침표가 처음이나 끝에 오면 제거하기
new_id = ".asdf.asdf."
new_id = re.sub("^[.]|[.]$", "", new_id)
# asdf.asdf
```



#### 내 코드 2 (정규표현식)

```python
import re

def solution(new_id):
    answer = ''
    # 1단계
    new_id = new_id.lower()
    # 2단계
    temp_list = re.findall("[a-z0-9-_.]+", new_id)
    new_id = "".join(temp_list)
    # 3단계
    new_id = re.sub("[.]{2,}", ".", new_id)
    # 4단계
    new_id = re.sub("^[.]|[.]$", "", new_id)
    # 5단계
    if len(new_id) == 0:
        new_id = "a"
    # 6단계
    if len(new_id) > 15:
        new_id = re.sub("[.]$", "", new_id[:15])
    # 7단계
    while len(new_id) < 3:
        new_id += new_id[-1]
    answer = new_id
    return answer
```



### 로또의 최고 순위와 최저 순위

#### 핵심 포인트

- 집합 자료형 (`set`)을 활용할 수 있는가?

#### 집합 자료형 (set)

```python
a_set = set([1, 2, 3])
b_set = set([2, 3, 4])
# 합집합
print(a_set + b_set)	# {1, 2, 3, 4}

# 차집합
print(a_set - b_set)	# {1}
print(b_set - a_set)	# {4}

# 교집합
print(a_set & b_set)	# {2, 3}

# 값 추가하기
# add
a_set.add(10)
print(a_set)			# {1, 2, 3, 10}

# update
b_set.update([10, 11, 12])
print(b_set)			# {2, 3, 4, 10, 11, 12}

# delete
b_set.remove(10)
print(b_set)			# {2, 3, 4, 11, 12}
```



#### 내 코드

```python
# 지워진 숫자가 모두 당첨숫자에 해당하는 경우
# 지워진 숫자가 모두 당첨숫자에 해당하지 않는 경우
# 즉, 남아있는 숫자 만으로 몇등에 해당하는 지 알아야 한다.
results = [6, 6, 5, 4, 3, 2, 1]
def solution(lottos, win_nums):
    answer = []
    # 집합 자료형: 교집합
    lotto_set = set(win_nums) & set(lottos)
    min_result = results[len(lotto_set)]
    max_result = results[len(lotto_set) + lottos.count(0)]
    answer = [max_result, min_result]
    return answer
```

