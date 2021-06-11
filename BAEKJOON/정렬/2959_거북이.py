# 거북이가 이동한 지점이 선분 그 자체가 아니다.
# 이동한 지점을 이은 것이 선분이 된다.
# 직사각형은 가로변과 세로변을 갖고 있다.
# 4개의 정수 중 2개는 가로 / 2개는 세로로 사용된다.
# 가로로 사용되는 2개의 정수 중 작은 것이 실제 직사각형의 가로 길이가 되며,
# 세로도 동일하다.
# 가장 작은 2개의 정수 중 작은 값과
# 나머지 2개의 정수 중 작은 값을 찾아보자.

def selectionSort(arr):
    # 0부터 N - 1까지 기준값을 정한다.
    for i in range(N - 1):
        # min_idx: 비교하는 요소들 중 가장 작은 값을 갖는 인덱스를 저장해둔다.
        min_idx = i
        for j in range(i + 1, N):
            if arr[j] < arr[min_idx]:
                min_idx = j
        else:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]


# 4개의 정수
N = 4
# 공백으로 구분된 4개의 정수를 배열에 담는다.
ARR = list(map(int, input().split()))
# 4개의 값을 정렬한다.
selectionSort(ARR)
a = ARR[0]
b = ARR[2]
print(a * b)