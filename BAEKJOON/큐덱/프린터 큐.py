# 가장 앞에 있는 문서의 중요도를 확인
# 뒤에 있는 문서들 중 중요도가 더 높은 게 있는지 확인
    # 1. 중요도가 높은 문서가 있다면, 그 문서의 인덱스만큼 앞에 있는 값을 맨 뒤로 옮긴다.
    # 2. 중요도가 높은 문서가 없다면 출력

TC = int(input())
for tc in range(TC):
    N, M = map(int, input().split())
    papers = list(map(int, input().split()))
    count = 0
    answer = 0

    while papers:
        highest_order = papers[0]
        next_idx = 0
        # 중요도 비교
        for idx in range(1, len(papers)):
            if highest_order < papers[idx]:
                next_idx = idx
                highest_order = papers[idx]
        for _ in range(next_idx):
            papers.append(papers.pop(0))
            M = M - 1 if M > 0 else len(papers) - 1
        papers.pop(0)
        count += 1
        if M == 0:
            answer = count
            break
        else:
            M -= 1
    print(answer)

