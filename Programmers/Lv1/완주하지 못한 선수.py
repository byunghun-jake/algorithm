def solution(participant, completion):
    answer = ''
    # 이름을 key로 갖는 dict 만들기
    people = {}
    for p in participant:
        if people.get(p):
            people[p] += 1
        else:
            people[p] = 1

    for c in completion:
        people[c] -= 1
        if people[c] == 0:
            del people[c]
    answer = list(people)[0]
    return answer