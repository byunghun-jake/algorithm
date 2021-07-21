import heapq
# 최대 힙을 구현해보자

# N: 연산 횟수
N = int(input())

heap = []

for _ in range(N):
    X = int(input())
    if X == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -X)



# class MaxHeap(object):
#     def __init__(self, items):
#         self.queue = [None] + items  # 0 번 인덱스 사용하지 않은 경우
#
#         # 절반의 노드만 heapify하면 됨
#         for i in range(len(self.queue) // 2, 0, -1):
#             self.max_heapify(i)
#
#     def parent(self, index):
#         return index // 2
#
#     def left_child(self, index):
#         return index * 2
#
#     def right_child(self, index):
#         return index * 2 + 1
#
#     def swap(self, i, parent_index):
#         self.queue[i], self.queue[parent_index] = self.queue[parent_index], self.queue[i]
#
#     def insert(self, n):
#         self.queue.append(n)
#         for i in range(len(self.queue) // 2, 0, -1):
#             self.max_heapify(i)
#
#     def delete(self):
#         last_index = len(self.queue) - 1
#         if last_index == 0:
#             return - 1  # empty
#
#         self.swap(1, last_index)
#         max_value = self.queue.pop()
#         self.max_heapify(1)  # root에서부터 재정렬
#         return max_value
#
#     # 임시 root 부터 자식 노드와 값을 비교하며 재정렬하는 함수
#     def max_heapify(self, i):
#         last_index = len(self.queue) - 1
#         left_index = self.left_child(i)
#         right_index = self.right_child(i)
#         temp_max_index = i  # 일단 자기 자신을 max로 둠 (임시 root노드)
#
#         # 리프 노드에 한해, 임시 루트 노드보다 값이 더 크면, 해당 노드의 인덱스를 루트 인덱스로 변경
#         if left_index <= last_index and self.queue[temp_max_index] < self.queue[left_index]:
#             temp_max_index = left_index
#         if right_index <= last_index and self.queue[temp_max_index] < self.queue[right_index]:
#             temp_max_index = right_index
#
#         # 만약 자신이 가장 큰게 아니면 heapify
#         if temp_max_index != i:
#             self.swap(i, temp_max_index)  # temp_max_index가 루트 노드로 변경
#             self.max_heapify(temp_max_index)  # 재정렬 재귀
#
#     def print_heap(self):
#         print(self.queue)
#
#
# heapq = MaxHeap([])
#
# for _ in range(N):
#     X = int(input())
#     if X == 0:
#         if len(heapq.queue) == 1:
#             print(0)
#         else:
#             print(heapq.delete())
#     else:
#         heapq.insert(X)



# Heap = [-1]

# 시간초과
# for _ in range(N):
#     X = int(input())
#
#     # 출력
#     if X == 0:
#         if len(Heap) <= 1:
#             print(0)
#         else:
#             print(Heap.pop())
#
#     # 입력
#     else:
#         idx = len(Heap)
#         Heap.append(X)
#         while idx != 1 and Heap[idx] < Heap[idx // 2]:
#             Heap[idx], Heap[idx // 2] = Heap[idx // 2], Heap[idx]
#             idx //= 2


# 시간초과
# for _ in range(N):
#     X = int(input())
#
#     # 출력할 값이 남아있지 않다면
#     if X == 0:
#         if len(Heap) == 1:
#             print(0)
#         else:
#             print(Heap.pop(1))
#
#     # 값을 입력한다면?
#     else:
#         idx = len(Heap)
#         Heap.append(X)
#         while idx != 1 and Heap[idx] > Heap[idx // 2]:
#             # 부모 노드와 값 교환
#             Heap[idx], Heap[idx // 2] = Heap[idx // 2], Heap[idx]
#
#             # 인덱스 변경
#             idx //= 2
