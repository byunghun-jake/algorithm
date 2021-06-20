# 시간 제한: 2초
# 메모리 제한: 256MB
# N: 20,000
# 문자의 길이는 최대 50 (1 ~ 50)

# 정렬 기준
    # 1. 길이가 짧은 것 부터
    # 2. 사전 순으로

# 같은 단어가 여러번 입력된 경우에는 한 번씩만 출력한다.
# 입력받은 값의 중복제거가 필요하다.
# 조합

import sys

def merge(left, right):
    result = []
    L = len(left)
    R = len(right)
    l_idx = r_idx = 0
    while l_idx < L and r_idx < R:



# 1~50 인덱스를 갖는 배열을 생성한 뒤, 입력받은 값의 길이를 파악해 해당하는 배열에 추가한다.
count_arr = [set()] * 51
for i in range(51):
    count_arr[i] = set()
# print(count_arr)

N = int(sys.stdin.readline().strip())

for _ in range(N):
    word = sys.stdin.readline().strip()
    count_arr[len(word)].add(word)
# print(count_arr)

for i in range(51):
    if len(count_arr[i]) == 0:
        continue
    words = list(count_arr[i])
    # words.sort()
    selectionSort(words, len(words))
    for word in words:
        print(word)
