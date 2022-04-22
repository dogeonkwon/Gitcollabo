# 2. ice_past, ice_present 두개를 만든다. ice_past 에서 0의 갯수를 센 다음
# ice_present 에 변화를 저장한다. 1년이 지나면 마지막 줄에 present 를 past 로 교체한다.
import sys

# sys.stdin = open('input.txt')
import copy
from collections import deque
def melting():
    ice_cnt = 0
    global ice_past, ice_present, point
    for i in range(N):
        for j in range(M):
            melt = 0
            # 빙산이라면
            if ice_past[i][j] > 0:
                # 동서남북 탐색해서 0의 갯수 파악
                for k in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    ni = i + k[0]
                    nj = j + k[1]

                    # 탐색 좌표가 범위 안에 들어왔고,
                    if 0 <= ni < N and 0 <= nj < M:

                        # 바다라면 melt+1 을한다.
                        if ice_past[ni][nj] == 0:
                            melt += 1

            # 인접한 바다(0)의 갯수만큼 빼준다.
            if ice_present[i][j] > melt:
                ice_present[i][j] -= melt
                ice_cnt += 1
                point = (i, j)
            else:
                ice_present[i][j] = 0

    ice_past = copy.deepcopy(ice_present)
    return ice_cnt

# front, rear 로 해보자
def BFS(p):
    visited = [[False]*M for _ in range(N)]

    front = -1
    rear = 0
    queue = deque()
    queue.append(p)
    visited[p[0]][p[1]] = True
    while front != rear:
        # print(queue)
        front += 1
        r = queue[front][0]
        c = queue[front][1]

        # print(r, c, queue, rear)

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

ice_past = [list(map(int, input().split())) for _ in range(N)]
ice_present = copy.deepcopy(ice_past)

point = ()

year = 1
while True:
    b = melting()
    if b == 0:
        year = 0
        break

    a = BFS(point)
    if len(a) != b:
        break

    else:
        year += 1

print(year)

# 빙하의 갯수와, 이어져 있는 빙하의 갯수가 같으면 한덩어리라는 의미