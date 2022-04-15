import sys
from collections import deque
sys.stdin = open('input.txt')

def BFS():
    global cnt, box

    # 하, 상, 뒤, 앞, 우, 좌
    dh = (1, -1, 0, 0, 0, 0)
    dr = (0, 0, 1, -1, 0, 0)
    dc = (0, 0, 0, 0, 1, -1)

    queue = deque()
    # 1이 있는 토마토의 위치를 찾고 그 좌표를 queue 에 넣는다.
    for h in range(H):          # 층
        for r in range(N):      # 행
            for c in range(M):  # 열
                if box[h][r][c] == 1:
                    queue.append([h, r, c])
    while queue:
        v = queue.popleft()
        # [0, 1, 3]
        # [0, 1, 4]
        # [0, 2, 3]
        # [0, 2, 4]
        for k in range(6):
            nh = v[0] + dh[k]
            nr = v[1] + dr[k]
            nc = v[2] + dc[k]

            # 탐색할 좌표가 범위안에 들어오고, 그곳이 덜 익은 토마토라면
            if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M and box[nh][nr][nc] == 0:
                # 그 토마토는 익고
                box[nh][nr][nc] = 1
                # 이 토마토에 영향을 준 토마토가 익기까지 걸린 시간에 +1 을 한다.
                cnt[nh][nr][nc] = cnt[v[0]][v[1]][v[2]] + 1
                queue.append((nh, nr, nc))

    # cnt 변화
    # [0, 0, 0, 1, 0],
    # [0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0]

    # [0, 0, 0, 1, 0],
    # [0, 0, 1, 0, 0],
    # [0, 0, 0, 0, 0]

    # [0, 0, 0, 1, 1],
    # [0, 0, 1, 0, 0],
    # [0, 0, 0, 0, 0]

    # [0, 0, 0, 1, 1],
    # [0, 0, 1, 0, 0],
    # [0, 0, 1, 0, 0]

    # [0, 0, 2, 1, 1],
    # [0, 0, 1, 0, 0],
    # [0, 0, 1, 0, 0]

    # [0, 0, 2, 1, 1],
    # [0, 0, 1, 0, 0],
    # [0, 2, 1, 0, 0]

    # [0, 0, 2, 1, 1],
    # [0, 0, 1, 0, 0],
    # [3, 2, 1, 0, 0]


# 덜 익은 과일이 있는지 확인 할 함수
def check(box):
    for h in range(H):  # 층
        for r in range(N):  # 행
            for c in range(M):  # 열
                if box[h][r][c] == 0:
                    return -1
    return 0

# M : 열, N : 행 , H : 층
M, N, H = list(map(int, input().split()))

# 토마토가 든 박스
box = list(list(list(map(int,input().split())) for _ in range(N)) for _ in range(H))

# 해당자리의 토마토가 며칠만에 익었는지 계산할 리스트
cnt = [[[0]*M for _ in range(N)] for _ in range(H)]
ans = 0

BFS()
a = check(box)

# 덜 익은 과일이 있다면 -1 출력
if a == -1:
    print(-1)

# 다 익었다면 며칠만에 다 익었는지 출력
else:
    for h in range(H):  # 층
        for r in range(N):  # 행
            for c in range(M):  # 열
                if cnt[h][r][c] > ans:
                    ans = cnt[h][r][c]
    print(ans)

