import sys
sys.stdin = open("input.txt")


def counting_sort(arr, N):
    # counting_sort를 이용해 정렬해보자
    # 최대값보다 1 큰 인덱스를 갖는 카운팅 배열
    c_arr = [0] * 101
    temp = [0] * N
    for i in range(N):
        c_arr[time_table[i]] += 1

    for i in range(len(c_arr) - 1, 0, -1):
        c_arr[i - 1] += c_arr[i]

    for i in range(N - 1, -1, -1):
        time = time_table[i]
        c_arr[time] -= 1
        idx = c_arr[time]
        temp[idx] = time

    return temp[:]


def selection_sort():
    # time_table = arr[:]
    N = len(time_table)
    for i in range(N-1):
        max_index = i
        for j in range(i+1, N):
            if time_table[max_index] < time_table[j]:
                max_index = j
        time_table[i], time_table[max_index] = time_table[max_index], time_table[i]
    # return time_table[:]


total_result = []

# T: 테스트 케이스 수
T = int(input())
for tc in range(1, T+1):
    # N: 손님 수
    # M: 붕어빵 만드는 데 소요되는 시간
    # K: 붕어 빵 개수
    N, M, K = map(int, input().split())

    is_possible = True

    # 손님 도착 시간 받기
    # 도착 시간은 순서대로 들어오지 않는다.
    time_table = list(map(int, input().split()))
    selection_sort()
    # end_time: 마지막 손님이 오는 시간
    end_time = time_table[0]
    start_time = time_table[-1]
    if start_time == 0:
        is_possible = False

    if is_possible:
        # 마지막 시간까지 붕어빵 장사 ㄱㄱ
        # bread_stack: 만들어진 붕어빵을 저장하는 곳
        bread_stack = []
        for time in range(1, end_time + 1):
            # 붕어빵 생성
            if time % M == 0:
                for _ in range(K):
                    bread_stack.append("붕어빵")

            # 손님 도착
            if time_table[-1] == time:
                # 붕어빵이 있으면,
                if bread_stack:
                    # 붕어빵을 줍니다.
                    bread_stack.pop()
                    # 손님이 갑니다.
                    time_table.pop()
                # 붕어빵이 없으면,
                else:
                    # 장사를 접습니다.
                    is_possible = False
                    break

    result = "Possible" if is_possible else "Impossible"

    total_result.append(f"#{tc} {result}")
    print(f"#{tc} {result}")































