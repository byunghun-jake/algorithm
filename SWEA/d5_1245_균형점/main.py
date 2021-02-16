# n개의 자성체가 1차원 공간에 존재
# 물체에 대한 자성체의 인력(F)
# F = G*m1*m2/(d*d)
# 물체에 작용하는 양쪽의 힘이 평형을 이루는 지점을 찾아보자
# n개의 자성체가 있다면 n-1개의 균형점이 존재한다
# 좌표값의 오차가 1e-12보다는 작아야 한다
import sys
sys.stdin = open("input.txt")

# 전체 테스트케이스 수
T = int(input())
for tc in range(1, T+1):
    # N: 자성체의 개수
    N = int(input())
    arr = list(map(int, input().split()))
    # X_list: 위치 배열
    # M_list: 질량 배열
    X = arr[:N]
    M = arr[N:]
    # 결과값의 개수: N-1
    result = []

    # 이진 탐색 (힌트)
    # 자성체의 모든 사이를 순환한다.
    for idx in range(N-1):
        # 양 끝에 있는 두 자성체의 좌표를 이용하여, 가운데 값을 찾아간다.
        left = X[idx]
        right = X[idx+1]
        # print(right, left)
        center = 0
        while (right - left) > 1 / 10**12:
            # print(right, left, center)
            # 중간 좌표 설정
            center = (right + left) / 2
            # 좌우 힘 초기화
            l_force = 0
            r_force = 0

            # 모든 자성체를 순환
            for i in range(N):
                # F = G*m1*m2/(d*d)
                force = M[i]/((X[i] - center)**2)
                if X[i] < center:
                    l_force += force
                else:
                    r_force += force

            # 좌우 힘 비교 (같을 때를 고려할 필요가 없음, 거리를 근사로 찾고 있기 때문에)
            if l_force > r_force:
                left = center
            else:
                right = center

        # 반복문 순환 후, 좌우 값 중 아무 값이나 넣어도 될 듯
        result.append(center)
        # result.append(left)
        # result.append(right)

    print(f"#{tc}", end=" ")
    for i in range(len(result)):
        print(f"{result[i]:.10f}", end=" ")
    print()


    































