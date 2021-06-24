# 원본 배열을 바꿔가며, 순열을 만들어보자.

arr = [1, 2, 3]
N = 3

def perm(idx):
    """
    :param idx: 자리를 바꿀 arr의 기준 인덱스
    """
    if idx == N - 1:
        print(arr)
        return

    for i in range(idx, N):
        arr[idx], arr[i] = arr[i], arr[idx]
        perm(idx + 1)
        arr[idx], arr[i] = arr[i], arr[idx]

perm(0)