def solution(table, languages, preference):
    answer = ''
    score_list = []
    for i in range(5):
        area_list = table[i].split()
        # 가지고 있는 언어에 따른 점수 계산
        score = 0
        for i in range(len(languages)):
            lan = languages[i]
            # list에 존재하는 지 확인 (index 메서드 에러 방지)
            if lan in area_list:
                score += (6 - area_list.index(lan)) * preference[i]
        score_list.append((area_list[0], score))
    # score_list 정렬
    score_list.sort(key=lambda x: (-x[1], x[0]))
    print(score_list)
    answer = score_list[0][0]
    return answer