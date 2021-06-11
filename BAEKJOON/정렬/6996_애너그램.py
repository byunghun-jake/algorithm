# 문제를 꼼꼼히 잘 읽어보자
# A에 속하는 알파벳 순서를 가지고 B를 만들 수 있다면?

# 두 문자를 다 정렬한 뒤 서로 같은 문자인지 확인한다.

N = int(input())
for _ in range(N):
    A, B = map(list, input().split())
    if sorted(A) == sorted(B):
        print(f"{''.join(A)} & {''.join(B)} are anagrams.")
    else:
        print(f"{''.join(A)} & {''.join(B)} are NOT anagrams.")