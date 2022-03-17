import sys
sys.stdin = open('input.txt')
from collections import deque

def BFS(s):
    queue = deque()
    queue.append(s)

    # 시작점을 True 로 바꾸고, 거리 1부터 시작
    visited[0][0] = True
    cnt[0][0] = 1

    while queue:
        # 현재 좌표를 담을 x, y
        x, y = queue.popleft()

        # 델타 탐색
        for k in range(4):
            # 현재 노드의 주위 노드를 탐색한다.
            nx, ny = x + dx[k], y + dy[k]
            # 새로 탐색할 노드가 범위 안에 들어왔고, 방문하지 않았고, 길이라면
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False and a[nx][ny] == 1:
                # queue 에 append 하고
                queue.append((nx, ny))
                # 부모 노드에 +1을 해서 레벨을 1 올린다.
                cnt[nx][ny] = cnt[x][y] + 1
                visited[nx][ny] = True

    print(cnt[n-1][m-1])

# 시작점이 root 가 되고, 연결 되어 있는 노드들은 자식노드로 생각한다.
# 도착점이 몇 레벨에 있는지 확인하면 최소 거리를 찾을 수 있다.

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(n)]

# 방문정보를 담을 리스트
visited = [[False] * m for _ in range(n)]

# 노드 간의 거리를 담을 리스트
cnt = [[0] * m for _ in range(n)]

BFS((0, 0))
