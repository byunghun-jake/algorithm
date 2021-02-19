# 42의 나머지를 담는 42 크기의 배열 생성
counting_list = [0]*42

count = 0

# 첫째 줄부터 열번째 줄까지 입력받기
for _ in range(10):
    num = int(input())
    remain = num % 42
    if counting_list[remain] == 0:
        count += 1
        counting_list[remain] += 1

print(count)