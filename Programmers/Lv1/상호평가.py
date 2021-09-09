def grading(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 50:
        return "D"
    return "F"


def solution(scores):
    answer = ''
    mean_arr = []
    # 자기 자신을 평가한 점수가 자기가 받은 점수 중 유일한 최고점 또는 유일한 최저점일 때 그 점수는 제외한다.
    scores_t = []
    l = len(scores)
    for c in range(l):
        score_list = []
        for r in range(l):
            score_list.append(scores[r][c])
        # 내가 준 점수와 최저점 / 최고점 비교
        min_score = min(score_list)
        max_score = max(score_list)
        score_sum = sum(score_list)
        student_count = l
        if score_list[c] == min_score and score_list.count(min_score) == 1:
            score_sum -= min_score
            student_count -= 1
        elif score_list[c] == max_score and score_list.count(max_score) == 1:
            score_sum -= max_score
            student_count -= 1
        mean_score = score_sum / student_count
        answer += grading(mean_score)

    return answer