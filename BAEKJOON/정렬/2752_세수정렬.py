# 띄어쓰기로 구분되어 들어오는 문자를 숫자 형태로 바꾸어 리스트에 저장한다.

# 버블정렬을 이용해, 숫자를 정렬한다.
def bubbleSort(arr):
    for i in range(2, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# 선택정렬을 이용해, 숫자를 정렬한다.
def selectionSort(arr):
    for i in range(N - 1):
        min_idx = i
        for j in range(i + 1, N):
            if arr[j] < arr[min_idx]:
                min_idx = j
        else:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]


# 카운팅 정렬
def countingSort(arr):
    # [3, 1, 2]
    counts = [0] * 1000000
    acc_counts = [0] * 1000000
    for i in range(N):
        counts[arr[i]] += 1
    for i in range(1000000 - 1):
        if i == 0:
            acc_counts[i] = counts[i]
        else:
            acc_counts[i] = acc_counts[i - 1] + counts[i]
    temp = [-1] * (N + 1)
    for i in range(N):
        temp[acc_counts[arr[i]]] = arr[i]
        acc_counts[arr[i]] -= 1
    return temp[1:]


N = 3
ARR = list(map(int, input().split()))
# bubbleSort(ARR)
# selectionSort(ARR)
# print(*ARR)
print(*countingSort(ARR))
