# 십진수 -> 이진수 변환
# 재귀 방식
    # 바닥 조건: 나누려는 숫자가 0 또는 1일 때 (2보다 작을 때)
    # 몫을 다음 함수의 인자로 전달하고, 나머지를 결과 배열에 추가한다.


def digit_to_binary(num):
    global result
    if num < 2:
        result.append(f"{num}")
        return

    digit_to_binary(num // 2)
    result.append(f'{num % 2}')



N = int(input())
result = []

digit_to_binary(N)
print("".join(result))
