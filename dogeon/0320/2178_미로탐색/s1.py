# 2178_미로탐색 풀이
# 2022-03-20

from collections import deque


def bfs(arr, n, m, visited):
    cnt = 1
    q = deque([[n, m, cnt]])                # 몇 번만에 도착했는지 체크하기 위해 cnt를 같이 추가
    visited[n][m] = cnt
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 델타탐색

    while q:
        v = q.popleft()

        cnt = v[2]

        rnr = v[0] + d[0][0]                # 오른쪽
        rnc = v[1] + d[0][1]

        dnr = v[0] + d[1][0]                # 아래
        dnc = v[1] + d[1][1]

        lnr = v[0] + d[2][0]                # 왼쪽
        lnc = v[1] + d[2][1]

        unr = v[0] + d[3][0]                # 위쪽
        unc = v[1] + d[3][1]

        if 0 <= rnr <= N and 0 <= rnc <= M and arr[rnr][rnc] == 1 and not visited[rnr][rnc]:   # 오른쪽으로 이동 하는데 범위안으로 들어오고, 이동할 수 있는곳인지 확인후, 방문한 적이 없다면 조건 성립
            q.append([rnr, rnc, cnt+1])                     # cnt+1 을 q에 추가해줌
            visited[rnr][rnc] = cnt + 1                     # cnt에 1을 더한 값을 저장해줌
        if 0 <= dnr <= N and 0 <= dnc <= M and arr[dnr][dnc] == 1 and not visited[dnr][dnc]:    # 아래쪽
            q.append([dnr, dnc, cnt + 1])
            visited[dnr][dnc] = cnt + 1
        if 0 <= lnr <= N and 0 <= lnc <= M and arr[lnr][lnc] == 1 and not visited[lnr][lnc]:    # 왼쪽
            q.append([lnr, lnc, cnt + 1])
            visited[lnr][lnc] = cnt + 1
        if 0 <= unr <= N and 0 <= unc <= M and arr[unr][unc] == 1 and not visited[unr][unc]:    # 위쪽
            q.append([unr, unc, cnt + 1])
            visited[unr][unc] = cnt + 1
        if visited[N][M]:
            break


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
N -= 1
M -= 1

bfs(arr, 0, 0, visited)

print(visited[N][M])                # 탐색이 끝났으면 목표 좌표의 값을 확인