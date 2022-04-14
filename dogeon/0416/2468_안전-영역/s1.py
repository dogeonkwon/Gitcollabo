# 2468_안전-영역 풀이
# 2022-04-16


def bfs(r, c):      # bfs로 갈 수 있는 곳을 탐색 후 조건에 맞다면 visited의 값을 n으로 바꿔줌
    q = [[r, c]]
    front = -1
    rear = 0
    while front < rear:
        front += 1
        vr = q[front][0]
        vc = q[front][1]
        for dr, dc in (0, 1), (1, 0), (0, -1), (-1, 0):
            nr = vr + dr
            nc = vc + dc
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] > n and visited[nr][nc] != n:
                visited[nr][nc] = n
                q.append([nr, nc])
                rear += 1


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
max_num = 1
ans = 1         # 비가 안내리는 경우도 있기 때문에 최소영역은 1

for k in range(N):              # 최대높이까지만 비가오는 것을 체크하면 됨
    for l in range(N):
        if max_num < arr[k][l]:
            max_num = arr[k][l]

for n in range(1, max_num):     # ans가 1이기 때문에 비가 내리는 경우는 1부터 건물의 최대 높이까지 고려
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > n and visited[i][j] != n:    # arr에서 비보다 건물 높이가 크고 visited에서 n과 값이 다르다면
                visited[i][j] = n       # visited에 표시를 하고 bfs탐색!
                bfs(i, j)
                cnt += 1
    if cnt > ans:
        ans = cnt

print(ans)