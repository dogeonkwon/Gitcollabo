# 1697_숨바꼭질 풀이
# 2022-03-12

from collections import deque


N, K = map(int, input().split())
queue = deque([N])
max_num = 100000                        # 런타임 에러를 막기위한 최대값
visited = [0 for _ in range(100001)]     # 각 자리 수를 몇 번 만에 도착하는지 알기 위한 리스트

while queue:                    # queue가 다 pop되면 종료
    n = queue.popleft()
    if n == K:                  # 그 전에 K 값을 찾게 된다면 몇 번(result[n])만에 찾게 되었는지 출력한 뒤 종료
        print(visited[n])
        break

    for m in (n+1, n-1, n*2):                   # 1초 뒤 +1, -1, *2가 되고 조건문에 걸리지 않는다면 result[m]의 값을 그 전값보다 +1 해서 저장한다.
        if 0 <= m <= max_num and not visited[m]:
            visited[m] = visited[n] + 1
            queue.append(m)                     # 그리고 queue에 추가하여 for문이 끝나면 다시 최근 추가되었던 값들을 pop하여 다시 찾는 값이 있는지 탐색한다.


## DFS로 풀려고 했는데 런타임 에러가 남
# def find(n, k, result):
#     global max_num
#     global lst
#
#     if result >= max_num:
#         return
#     elif n < 0:
#         return
#     elif n == k:
#         lst += [result]
#         max_num = result
#         return
#     else:
#         result += 1
#         for i in range(3):
#             if i == 0:
#                 n += 1
#                 find(n, k, result)
#                 n -= 1
#             elif i == 1:
#                 n -= 1
#                 find(n, k, result)
#                 n += 1
#             else:
#                 n *= 2
#                 find(n, k, result)
#                 n //= 2
#
#
# N, K = map(int, input().split())
# result = 0
# max_num = 100000
# visited = list()
# lst = list()
# find(N, K, result)
#
# print(min(lst))