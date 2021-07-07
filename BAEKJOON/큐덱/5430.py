import sys

TC = int(sys.stdin.readline().strip())

for tc in range(TC):
    operations = sys.stdin.readline().strip()
    N = int(sys.stdin.readline().strip())
    NUMS = sys.stdin.readline().strip()[1:-1].split(",")
    is_front_pop = True
    start_idx = 0
    end_idx = N
    for operation in operations:
        if operation == "R":
            is_front_pop = not is_front_pop
        else:
            if end_idx <= start_idx:
                print("error")
                break
            if is_front_pop:
                start_idx += 1
            else:
                end_idx -= 1
    else:
        answer = NUMS[start_idx:end_idx]
        if not is_front_pop:
            answer = answer[::-1]

        print(f"[{','.join(answer)}]")

# for tc in range(TC):
#     operations = sys.stdin.readline().strip()
#     N = int(sys.stdin.readline().strip())
#     NUMS = sys.stdin.readline().strip()[1:-1]
#     direction = True
#     if len(NUMS) < 1:
#         num_list = []
#     else:
#         num_list = list(map(int, NUMS.split(",")))
#     for operation in operations:
#         if operation == "R":
#             direction = not direction
#             # num_list = num_list[::-1]
#         elif operation == "D":
#             if len(num_list) < 1:
#                 print("error")
#                 break
#             # num_list.pop(0)
#             if direction:
#                 num_list.pop(0)
#             else:
#                 num_list.pop()
#     else:
#         if not direction:
#             num_list = num_list[::-1]
#         print(f"[{','.join(list(map(str, num_list)))}]")
