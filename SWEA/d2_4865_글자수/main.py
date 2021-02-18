# str1에 있는 글자를 중복되지 않도록 배열에 담는다.
# 글자가 담긴 배열과 같은 크기의 카운팅 배열을 만든다.
# str2에 있는 글자를 순환하며, 같은 글자를 찾았을 때 같은 인덱스의 카운팅 배열에 1을 더한다.
import sys

sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    # str1: 기준 문자열
    # str2: 탐색 대상 문자열의 문자 배열
    str1 = input()
    str2 = list(input())

    # str1 문자열의 문자를 중복없이 배열에 담는다.
    check_list = []
    for i in range(len(str1)):
        # set을 사용해도 되지만, 반복문을 다시 사용하는 것으로 한다.
        is_duplicated = False
        # check_list를 순환하며, 중복 여부를 체크한다.
        for j in range(len(check_list)):
            if check_list[j] == str1[i]:
                is_duplicated = True
                break
        # 중복이 있다면, str1의 다음 문자로 넘어간다
        if is_duplicated:
            continue
        # 중복이 없다면, check_list에 추가한다.
        check_list.append(str1[i])
    # print(check_list)
    # 카운팅 배열을 생성한다.
    counting_list = [0] * len(check_list)

    # str2를 순환하며, 문자를 센다
    # 카운팅 배열에 값을 추가하며, 최대값을 찾는다.
    max_count = 0
    for word in str2:
        for idx in range(len(check_list)):
            if word == check_list[idx]:
                counting_list[idx] += 1
                if max_count < counting_list[idx]:
                    max_count = counting_list[idx]

    print(f"#{tc} {max_count}")

































