# 17070_파이프옮기기1 풀이
# 2022-04-05

# dfs도 시간초과....
def dfs(r, c, d):
    global cnt

    if r == N-1 and c == N-1 and not arr[r][c]:
        cnt += 1
        return

    if d != 3:
        if c+1 < N:
            if not arr[r][c+1]:
                dfs(r, c+1, 1)

    if r+1 < N and c+1 < N:
        if not arr[r][c+1] and not arr[r+1][c+1] and not arr[r+1][c]:
            dfs(r+1, c+1, 2)

    if d != 1:
        if r+1 < N:
            if not arr[r+1][c]:
                dfs(r+1, c, 3)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
dfs(0, 1, 1)
print(cnt)


## bfs 풀이(시간 초과)
# q = [[0, 1, 1]]
# front = -1
# rear = 0
# while front != rear:
#     front += 1
#     v = q[front]
#
#     if 0 <= v[1]+1 < N and not arr[v[0]][v[1]+1] and (v[2] == 1 or v[2] == 2):       # 오른쪽 (1)
#         if v[0] == N-1 and v[1]+1 == N-1:
#             cnt += 1
#         elif v[1]+1 == N-1:
#             result += 1
#         else:
#             q.append([v[0], v[1]+1, 1])
#             rear += 1
#
#         # 대각선 (2)
#     if 0 <= v[0]+1 < N and 0 <= v[1]+1 < N and not arr[v[0]][v[1]+1] and not arr[v[0]+1][v[1]+1] and not arr[v[0]+1][v[1]]:
#         if v[0]+1 == N-1 and v[1]+1 == N-1:
#             cnt += 1
#         else:
#             q.append([v[0]+1, v[1]+1, 2])
#             rear += 1
#
#     if 0 <= v[0]+1 < N and not arr[v[0]+1][v[1]] and (v[2] == 3 or v[2] == 2):   # 아래 (3)
#         if v[0]+1 == N-1 and v[1] == N-1:
#             cnt += 1
#         elif v[0]+1 == N-1:
#             result += 1
#         else:
#             q.append([v[0]+1, v[1], 3])
#             rear += 1

