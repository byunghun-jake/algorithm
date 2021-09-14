max_score = 0


def solution(land):
    answer = 0
    N = len(land)

    def ddang(cr, bc, total_score):
        global max_score
        if cr == N:
            max_score = max(total_score, max_score)
            return
        for cc in range(4):
            if cc == bc:
                continue
            return ddang(cr + 1, cc, total_score + land[cr][cc])

    ddang(0, 5, 0)
    answer = max_score

    return answer

solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]])