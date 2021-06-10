# 자연수 N이 주어질 때, N을 이진수로 변환하는 프로그램을 작성하시오.

# 재귀 방식으로 풀려면?
# 받는 인자 => 소인수분해 할 숫자
# 종료 조건 => 숫자가 0일 때,
# 다음 단계 => 소인수분해 후 몫을 인자로 전달한다.
# 소인수분해 한 후 나머지를 누적한다.

def recursive(num):
    if num == 0:
        return

    n = recursive(num // 2)
    if n:
        return str(n) + str(num % 2)
    else:
        return str(num % 2)

print(recursive(int(input())))