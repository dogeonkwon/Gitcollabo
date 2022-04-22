# 2573_빙산
# 2022-04-13
# 시간 초과


# bfs
def bfs(si, sj):
    global year
    melting = [[0] * M for _ in range(N)]
    queue = [(si, sj)]
    front = -1
    rear = 0

    while front < rear:
        front += 1
        n, m = queue[front]
        ices[n][m] = year

        for dn, dm in (1, 0), (0, 1), (-1, 0), (0, -1):
            cn = n+dn
            cm = m+dm

            if 0 <= cn < N and 0 <= cm < M:
                if not arr[cn][cm]:
                    melting[n][m] += 1
                else:
                    if (cn, cm) not in queue:
                        queue.append((cn, cm))
                        rear += 1

    return Melt(melting)


def Melt(melt):
    global year

    for p in range(1, N-1):
        for q in range(1, M-1):
            if arr[p][q] and ices[p][q] != year:
                return True

            if melt[p][q]:
                if arr[p][q] - melt[p][q] < 0:
                    arr[p][q] = 0
                else: arr[p][q] -= melt[p][q]

    return False


N, M = map(int, input().split())  # N: 행, M: 열
arr = [list(map(int, input().split())) for _ in range(N)]   # 빙산의 정보
ices = [[0] * M for _ in range(N)]   # 빙산이 있는 위치
result = 0
year = 0

while True:
    year += 1
    c = 0
    for n in range(1, N-1):
        for m in range(1, M-1):
            if arr[n][m]:
                c = 1
                if bfs(n, m):
                    result = year
                    break
        if c:
            break

    if result == year or not c:
        break

print(result)