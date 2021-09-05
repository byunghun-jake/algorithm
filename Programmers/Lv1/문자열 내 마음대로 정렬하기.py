# sort 메서드에서 2개 이상의 key를 갖는 정렬 구현하기

def solution(strings, n):
    answer = sorted(strings, key=lambda x: (x[n], x))
    return answer