# 부분집합 구하기
ARR = [1, 2, 3, 4]
def powerSet_loop():
    bit = [0, 0, 0, 0]
    for i in range(2):
        bit[0] = i
        for j in range(2):
            bit[1] = j
            for k in range(2):
                bit[2] = k
                for l in range(2):
                    bit[3] = l
                    print(bit)
                    for idx in range(4):
                        if bit[idx]:
                            print(ARR[idx], end="")
                    print()

# powerSet_loop()

# 비트
ARR = [1, 2, 3, 4]
def powerSet_bit():
    count = 0
    for i in range(1 << len(ARR)):
        for j in range(i):
            count += 1
            if j > len(ARR):
                break
            if i & (1 << j):
                print(ARR[j], end="")
        print()
    print(count)

# powerSet_bit()


# 백트래킹

# N: 기준 배열의 길이
# arr: 기준 배열
# sel: 해당 원소를 뽑기로 했는지 저장하는 배열
N = 3
arr = [1, 2, 3]
sel = [0] * N

def powerSet_backtracking(idx):
    if idx == N:
        print(*sel)
        for i in range(N):
            if sel[i]:
                print(arr[i], end=" ")
        print()
        return

    sel[idx] = 0
    powerSet_backtracking(idx + 1)
    sel[idx] = 1
    powerSet_backtracking(idx + 1)

powerSet_backtracking(0)