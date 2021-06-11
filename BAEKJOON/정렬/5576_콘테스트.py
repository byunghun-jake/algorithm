# 앞 10개 줄은 W대학
# 뒤 10개 줄은 K대학
# 각각 반복문을 통해 값을 저장해나간 뒤 각각 상위 3명의 학생 점수를 더한 값을 출력하자.

def countingSort(arr):
    counting = [0] * 101
    for i in range(10):
        counting[arr[i]] += 1
    for i in range(1, 101):
        counting[i] += counting[i - 1]
    temp = [-1] * 11
    for i in range(9, -1, -1):
        temp[counting[arr[i]]] = arr[i]
        counting[arr[i]] -= 1
    return temp[1:]

W_list = [int(input()) for _ in range(10)]

K_list = [int(input()) for _ in range(10)]

W = sum(countingSort(W_list)[7:])
K = sum(countingSort(K_list)[7:])

print(W, K)