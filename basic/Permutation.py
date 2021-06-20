# {1, 2, 3}을 포함하는 모든 순열을 생성하는 함수
for i1 in range(1, 4):
    for i2 in range(1, 4):
        if i1 == i2:
            continue
        for i3 in range(1, 4):
            if i1 == i3 or i2 == i3:
                continue
            print(i1, i2, i3)

# 백트래킹을 이용해 순열 구하기
def perm_back(arr, k, count):
    # arr: 원본 배열
    # k: 