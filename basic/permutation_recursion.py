arr = [1, 2, 3]

N = 3

sel = [0] * N       # 결과들이 저장될 리스트
check = [0] * N     # 해당 원소를 사용했는지, 안했는지 체크


def perm(idx):
    # 다 뽑았다면?
    if idx == N:
        print(sel)
    else:
        for i in range(N):
            if check[i] == 0:       # i번째 원소를 사용하지 않았다면,
                sel[idx] = arr[i]   # idx 위치에 i번째 원소를 넣는다.
                check[i] = 1        # i번째 원소를 사용했음!
                perm(idx + 1)
                
                # sel[idx]를 원상복구시키지 않는 이유: 다음 값으로 덮어씌워질 것이기 때문에
                check[i] = 0        # i번째 원소를 사용하지 않았을 때로 복구
                



perm(0)