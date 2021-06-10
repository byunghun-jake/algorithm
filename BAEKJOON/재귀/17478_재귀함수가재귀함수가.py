# 들여쓰기를 구현할 것
# 반환할 값은 없이 바로 출력
# 이스케이프 문자도 활용
# 마지막에 답변하는 부분이 있다.

def recursive(num):
    before = "_" * num * 4
    if num == 0:
        print(f"{before}어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
    if num == N:
        print(f"{before}\"재귀함수가 뭔가요?\"")
        print(f"{before}\"재귀함수는 자기 자신을 호출하는 함수라네\"")
        print(f"{before}라고 답변하였지.")
        return

    print(f"{before}\"재귀함수가 뭔가요?\"")
    print(f"{before}\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.")
    print(f"{before}마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
    print(f"{before}그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"")
    recursive(num + 1)
    print(f"{before}라고 답변하였지.")

N = int(input())
recursive(0)