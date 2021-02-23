import sys

sys.stdin = open("input.txt")

# T: 테스트케이스 수
T = int(input())

for tc in range(1, T+1):
    # 메모리 원래 값
    memory = list(map(int, list(input())))
    L = len(memory)
    # 맨 앞자리부터 순회하며, 숫자가 바뀔 때 마다 1씩 카운트
    before_num = 0
    count = 0
    for num in memory:
        if num != before_num:
            count += 1
            before_num = num
    print(f"#{tc} {count}")


























