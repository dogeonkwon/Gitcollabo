# 2468_안전영역
# 2022-04-13


def bfs(si, sj, K):
    visited[si][sj] = 1
    queue = [(si, sj)]
    front = -1
    rear = 0

    while front < rear:
        front += 1
        n, m = queue[front]

        for dn, dm in (1, 0), (-1, 0), (0, 1), (0, -1):
            cn = n + dn
            cm = m + dm

            if 0 <= cn < N and 0 <= cm < N and arr[cn][cm] > K and not visited[cn][cm]:
                visited[cn][cm] = 1
                queue.append((cn, cm))
                rear += 1


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 1   # 비가 안오는 경우 result = 1
h = 1

# 가장 높은 건물의 높이 구하기
for p in range(N):
    for q in range(N):
        if arr[p][q] > h:
            h = arr[p][q]


# 강수량을 변화시키면서 잠기지 않는 구역의 개수 구하기
for k in range(1, h):
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > k and not visited[i][j]:
                cnt += 1
                bfs(i, j, k)

    if cnt > result:
        result = cnt

print(result)