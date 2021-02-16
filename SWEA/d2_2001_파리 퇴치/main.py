# 파리채가 배열을 벗어나면 손해(고려하지 않음)
import sys

sys.stdin = open("input.txt")

# 전체 테스트 개수
T = int(input())
for tc in range(1, T+1):
    # N: 파리 배열 크기
    # M: 파리채 배열 크기
    N, M = map(int, input().split())

    # 파리 배열 입력받기
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    # 파리채 좌상단 위치 범위 설정
    # end 위치 설정
    start = 0
    end = N - M

    # 좌상단 위치를 옮겨가는 반복문
    # max_count: 파리 최대 마리수
    max_count = 0
    for r in range(start, end+1):
        for c in range(start, end+1):
            # count: 파리 합
            count = 0
            # 기준점으로 부터 정해진 영역에 대한 파리의 마리수 세기
            for fr in range(r, r+M):
                for fc in range(c, c+M):
                    count += arr[fr][fc]
            # max_count와 비교
            if count > max_count:
                max_count = count

    print(f"#{tc} {max_count}")
































