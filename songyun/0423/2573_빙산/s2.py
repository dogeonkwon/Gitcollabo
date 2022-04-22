import copy
from collections import deque

def melting():
    ice_cnt = 0



# front, rear 로 해보자
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

ice_past = [list(map(int, input().split())) for _ in range(N)]
ice_present = copy.deepcopy(ice_past)

point = ()

for i in range(N):
    for j in range(M):


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