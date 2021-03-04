import sys

sys.stdin = open("./input.txt")

N = int(input())

num_list = list(map(int, input().split()))


def bubble_sort(n_list):
    for i in range(len(n_list), 0, -1):
        for j in range(i - 1):
            if n_list[j] > n_list[j+1]:
                n_list[j], n_list[j+1] = n_list[j+1], n_list[j]
    return n_list[:]


sorted_list = bubble_sort(num_list[:])
index = N // 2

print(sorted_list[index])