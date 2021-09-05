import re


def solution(dartResult):
    answer = 0
    score_list = [0, 0, 0]
    minus_plus_list = [1, 1, 1]
    double_list = [0, 0, 0]
    idx = 0
    set_p = re.compile("[0-9]*[SDT][#*]*")
    score_p = re.compile("[0-9]*")
    bonus_p = re.compile("[SDT]")
    option_p = re.compile("[#*]")
    for i in range(3):
        m = set_p.match(dartResult[idx:])
        text = m.group()
        t_i = 0
        score = score_p.match(text).group()
        t_i += len(score)
        score = int(score)
        bonus = bonus_p.match(text[t_i:]).group()
        t_i += 1
        option_m = option_p.match(text[t_i:])

        if bonus == "D":
            score **= 2
        elif bonus == "T":
            score **= 3
        score_list[i] = score

        # 옵션 찾기
        if option_m:
            option = option_m.group()
            # 스타상
            if option == "*":
                double_list[i] += 1
                if i - 1 > -1:
                    double_list[i - 1] += 1
            # 아차상
            elif option == "#":
                minus_plus_list[i] = -1
        idx += len(text)
    for i in range(3):
        answer += score_list[i] * minus_plus_list[i] * (2 ** double_list[i])
    return answer

print(solution("1D2S#10S"))