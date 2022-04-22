# 2573_빙산 풀이
# 2022-04-23


def bfs(r, c):

    front = -1
    rear = 0
    q = [[r, c]]

    while front < rear:
        front += 1
        vr = q[front][0]
        vc = q[front][1]
        for dr, dc in (0, 1), (1, 0), (0, -1), (-1, 0):     # 델타 탐색
            nr = vr + dr
            nc = vc + dc

            if arr[nr][nc] > 0 and visited[nr][nc] != year:     # 이동할 위치에 빙산이 존재하고 체크한 적이 없다면
                visited[nr][nc] = year
                q.append([nr, nc])
                rear += 1
            elif arr[nr][nc] <= 0 and visited[nr][nc] != year and arr[vr][vc]:  # 이동할 위치가 바다이고 체크한 적이 없으며 현재 위치에 빙산이 존재한다면
                arr[vr][vc] -= 1


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

cnt = 1     # 빙산의 개수가 2개 이상으로 나뉘었는지 체크해줌
year = 1    # 연도

while cnt == year:          # 2개 이상으로 나뉘지 않았다면 cnt와 year는 +1씩 커지므로 달라지는 순간 2개 이상으로 나뉜거임 혹은 두 덩어리 이상으로 분리되지 않은 것
    for i in range(1, N-1):     # 첫 행,열 / 마지막 행,열 은 어차피 바다이므로 탐색할 필요 없음
        for j in range(1, M-1):
            if arr[i][j] and visited[i][j] != year:     # 빙산이 존재하고 이번년도에 체크한 적이 없다면
                visited[i][j] = year     # 체크 해주고
                bfs(i, j)       # 탐색 시작!
                cnt += 1        # cnt가 2이상 더해지면 두 개로 나뉘었다는 의미임
    year += 1       # year는 전체 반복문이 돌아갈 동안 +1만 됨

if cnt > year:      # 두 개 이상으로 나뉘어졌을 경우
    print(year-2)
else:           # 두 덩어리 이상으로 분리되지 않은 것
    print(0)