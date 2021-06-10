# 두 정수 A, B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오

# ,로 구분되어 들어오는 두 정수를 나누어준다.
# 형 변환을 한 뒤 더한 값을 출력한다.

N = int(input())

for tc in range(N):
    A, B = map(int, input().split(","))
    print(A + B)