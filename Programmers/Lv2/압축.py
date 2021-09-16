def reset_dic(dic):
    for o in range(ord("A"), ord("Z") + 1):
        dic[chr(o)] = o - ord("A") + 1

def solution(msg):
    dic = {}
    answer = []
    reset_dic(dic)
    i = 0
    while i < len(msg):
        l = 0
        while dic.get(msg[i:i + l + 1]):
            print(dic.get(msg[i:i + l + 1]))
            l += 1
        w = msg[i:i + l]
        c = msg[i + l]
        # 출력
        answer.append(dic[w])
        # 사전 추가
        dic[w + c] = len(dic) + 1
        # 인덱스 업데이트
        i = i + l
    return answer

solution("KAKAO")