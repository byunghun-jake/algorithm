def my_sum(n):
    result = n + sum(map(int, list(str(n))))
    # while n:
    #     result += n % 10
    #     n //= 10
    # print(result)
    return result


N = 10000
self_sum_list = []
remove_list = set([num + sum(map(int, list(str(num)))) for num in range(1, N)])
# for num in range(1, N):
#     self_sum = my_sum(num)
#     # if self_sum > 10000:
#     #     break
#     self_sum_list.append(self_sum)
#     # print(self_sum)

result = {*range(1, N)} - remove_list

for num in sorted(result):
    print(num)

























