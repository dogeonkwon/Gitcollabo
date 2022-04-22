import copy
from collections import deque

def melting():
    ice_cnt = 0 # 빙하 갯수
    global ice_past, ice_present, point

    for i in range(N):
        for j in range(M):
            melt = 0 # 빙하를 둘러싼 바다칸 갯수

            # 빙산이라면
            if ice_past[i][j] > 0:
                # 동서남북 탐색해서 바다의 갯수 파악
                for k in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    ni = i + k[0]
                    nj = j + k[1]

                    # 탐색 좌표가 범위 안에 들어왔고,
                    if 0 <= ni < N and 0 <= nj < M:

                        # 바다라면 melt+1 을 한다.
                        if ice_past[ni][nj] == 0:
                            melt += 1

            # 인접한 바다(0)의 갯수만큼 빼준다.
            if ice_present[i][j] > melt:
                ice_present[i][j] -= melt
                # 1년이 지난 후 살아있는 빙하의 수 카운트
                ice_cnt += 1

                point = (i, j)

            # 빙하의 높이 보다 바다의 수가 더 많다면 빙하의 높이는 0으로 만든다.
            else:
                ice_present[i][j] = 0

    # 다음 비교를 위해 ice_past 갱신
    ice_past = copy.deepcopy(ice_present)
    return ice_cnt


# 빙하가 두 덩이 이상으로 나눠졌는지 확인할 함수
# 1. melting 함수에서 살아있는 빙하 중 한개의 좌표를 ice_point 로 받아온다.
# 2. 해당 좌표의 빙하와 연결된 빙하의 수(len(queue))를 파악한다.
# 2. 남은 빙하의 수 (ice_cnt)와 비교해서 둘의 갯수가 같다면 한덩이라는 의미.
def BFS(p):
    visited = [[False]*M for _ in range(N)]

    front = -1
    rear = 0
    queue = deque()
    queue.append(p)
    visited[p[0]][p[1]] = True
    while front != rear:
        front += 1
        r = queue[front][0]
        c = queue[front][1]


        # 주위에 빙산이 있는지 탐색
        for k in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nr = r + k[0]
            nc = c + k[1]

            if 0 <= nr < N and 0 <= nc < M:

                # 탐색 좌표에 빙산이 있으면
                if ice_present[nr][nc] > 0 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    # 그 빙산을 queue 에 넣는다.
                    queue.append((nr, nc))
                    rear += 1

    return queue


N, M = map(int, input().split())

# ice_past = 1년이 지나기 전 빙하상태
# ice_present = 1년 지난 후 빙하 상태
#
ice_past = [list(map(int, input().split())) for _ in range(N)]
ice_present = copy.deepcopy(ice_past)

point = ()

year = 1
while True:
    b = melting() # 남은 빙하의 수
    if b == 0:
        year = 0
        break

    a = BFS(point)  # 임의의 한 빙하와 연결된 빙하의 수
    if len(a) != b: # 둘의 크기가 다르면 두 덩이 이상으로 나눠졌다는 의미
        break

    # 아직 한덩이라면 1년 더 지켜본다.
    else:
        year += 1

print(year)

# 빙하의 갯수와, 이어져 있는 빙하의 갯수가 같으면 한덩어리라는 의미