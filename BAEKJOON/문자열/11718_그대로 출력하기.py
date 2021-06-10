# 입력받은 그대로 출력하는 프로그램

# 입력을 받는 무한 반복문을 사용
# 입력이 들어오지 않았을 때, break

# 읽어들일 데이터가 더 이상 없을 때에는 EOFError가 발생한다.

while True:
    try:
        text = input()
        print(text)
    except EOFError:
        break