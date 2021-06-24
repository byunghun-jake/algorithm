# 비트 연산을 이용해 순열을 구현하자

# N개의 원소로 이루어진 배열에서 M개를 뽑아 순열을 만든다면?

# 뽑은 숫자를 저장하는 배열: sel
# 숫자를 사용했는지 확인하는 방법: check & (1 << j)

arr = [1, 2, 3, 4]
N = 4
M = 4

sel = [0] * M

def perm_bit(idx, check):
    """
    비트를 이용한 순열 구현
    :param idx: 현재 컨트롤할 sel의 인덱스
    :param check: 값을 사용했는지 저장하는 10진수 숫자
    """
    if idx == M:
        print(*sel)
        return

    for i in range(N):
        if check & (1 << i): continue
        sel[idx] = arr[i]
        perm_bit(idx + 1, check | (1 << i))

perm_bit(0, 0)