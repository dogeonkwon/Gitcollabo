# 2573 빙산
# 2022-04-20


# bfs
def bfs(sn, sm):
    global year, visited, cnt, si, sj
    queue = [(sn, sm)]    # queue 초기값
    melting = [0]         # queue의 빙하가 녹는 양      ex> queue[0] 빙하는 melting[0]만큼 녹는다 !
    front = -1
    rear = 0

    while front < rear:
        front += 1
        n, m = queue[front]
        visited[n][m] = year

        # 델타 탐색
        for dn, dm in (1, 0), (0, 1), (-1, 0), (0, -1):
            if 0 <= n+dn < N and 0 <= m+dm < M:
                if not arr[n+dn][m+dm]:    # 빙하가 없다면
                    melting[front] += 1    # 1만큼 추가로 녹일 수 있다

                else:
                    # 그 해에 방문한 적 없을 때
                    if visited[n+dn][m+dm] != year:
                        visited[n + dn][m + dm] = year   # 방문표시
                        queue.append((n+dn, m+dm))       # queue에 좌표 추가
                        melting.append(0)                # 녹는 양 정보 추가
                        rear += 1

    # 두 덩어리로 쪼개져있는 경우
    # 전년도에 두 덩어리로 쪼개졌음을 알 수 있다 !
    if cnt != len(queue):
        return True

    # 빙하 녹이기
    v = cnt
    for c in range(v):
        p, q = queue[c][0], queue[c][1]

        # 빙하가 다 녹지 않는 경우
        if arr[p][q] - melting[c] > 0:
            arr[p][q] -= melting[c]  # 빙하를 녹이고
            si, sj = p, q            # 다음 bfs시 시작할 값을 정해준다
            continue

        # 빙하가 다 녹을 경우, cnt - 1
        arr[p][q] = 0
        cnt -= 1

    return False


N, M = map(int, input().split())  # N: 행, M: 열
arr = [list(map(int, input().split())) for _ in range(N)]   # 빙산의 정보
visited = [[0]*M for _ in range(N)]   # 방문표시
result = 0      # 결과
year = 0        # 녹는 시간 카운팅
cnt = 0         # 빙하의 개수 카운팅
si, sj = 0, 0   # 빙하의 좌표 >> bfs로 탐색하기 때문에 어떤 빙하에서 시작해도 상관없다 !!


# 빙산의 개수 구하기
for i in range(1, N-1):
    for j in range(1, M-1):
        if arr[i][j]:
            cnt += 1
            si, sj = i, j

while True:
    year += 1

    # 놓친 부분 !!
    # 녹을 빙하가 없다면 굳이 bfs를 할 필요가 없다 !
    if not cnt:
        break

    if bfs(si, sj):
        result = year-1   # year + 1로 시작하기 때문에 -1을 해준다 !
        break

print(result)