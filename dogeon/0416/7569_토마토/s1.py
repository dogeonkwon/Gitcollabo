# 7569_토마토 풀이
# 2022-04-16

from collections import deque

M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]


flag = ans = 0
q = deque()

for h in range(H):      # 3차원으로 접근(2차원으로 할 경우 테케의 2번 인덱스 줄과 3번 인덱스 줄의 간섭이 일어난다. 일어나면 안됨, 2차원으로 하려면 더 많은 조건을 넣어야함)
    for i in range(N):
        for j in range(M):
            if arr[h][i][j] == 1:
                q.append((h, i, j))     # arr의 값이 1인 것들을 다 q에 담아준다.

while q:
    v0, v1, v2 = q.popleft()
    for dh, dr, dc in (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, -1), (0, 0, 1):   # 위, 아래, 앞, 뒤, 좌, 우
        nh = v0 + dh
        nr = v1 + dr
        nc = v2 + dc
        if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M and arr[nh][nr][nc] == 0:
            arr[nh][nr][nc] = arr[v0][v1][v2] + 1   # 누적합
            q.append((nh, nr, nc))

for k in range(H):          # 탐색이 다 끝났다면
    for n in range(N):
        for m in range(M):
            if arr[k][n][m] == 0:   # 0이 있는지 체크
                flag = 1
            elif arr[k][n][m] > ans:    # 최대값 체크
                ans = arr[k][n][m]
        if flag:
            break
    if flag:        # 0이 있다면 -1 출력
        print(-1)
        break

if not flag and ans == 1:   # 최대값이 그대로라면 0 출력
    print(0)
elif not flag:  # 위의 조건들을 다 통과했다면 최대값 출력
    print(ans-1)



# 1차 시도
'''
nput().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]


front = rear = -1
zero = plus = minus = ans = 0
q = [[] for _ in range(1000000)]

for h in range(H):
    for i in range(N):
        for j in range(M):
            if arr[h][i][j] == 1:
                rear += 1
                q[rear] = ([h, i, j])
                plus += 1
            if arr[h][i][j] == -1:
                minus += 1
            if arr[h][i][j] == 0:
                zero += 1


if minus + plus == N*M*H:
    print(0)
elif plus:
    while front < rear:
        front += 1
        v = q[front]
        for dh, dr, dc in (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, -1), (0, 0, 1):   # 위, 아래, 앞, 뒤, 좌, 우
            nh = v[0] + dh
            nr = v[1] + dr
            nc = v[2] + dc
            if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M and arr[nh][nr][nc] == 0:
                arr[nh][nr][nc] = arr[v[0]][v[1]][v[2]] + 1
                rear += 1
                q[rear] = [nh, nr, nc]
                zero -= 1
                if arr[nh][nr][nc] > ans:
                    ans = arr[nh][nr][nc]-1
    if zero:
        print(-1)
    else:
        print(ans)

elif not plus:
    print(-1)
'''



# 2차 시도
'''
M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]


front = rear = -1
flag = ans = 0
q = list()

for h in range(H):
    for i in range(N):
        for j in range(M):
            if arr[h][i][j] == 1:
                q.append([h, i, j])
                rear += 1


while front < rear:
    front += 1
    v0, v1, v2 = q[front]
    for dh, dr, dc in (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, -1), (0, 0, 1):   # 위, 아래, 앞, 뒤, 좌, 우
        nh = v0 + dh
        nr = v1 + dr
        nc = v2 + dc
        if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M and arr[nh][nr][nc] == 0:
            arr[nh][nr][nc] = arr[v0][v1][v2] + 1
            q.append([nh, nr, nc])
            rear += 1


for k in range(H):
    for n in range(N):
        for m in range(M):
            if arr[k][n][m] == 0:
                flag = 1
            elif arr[k][n][m] > ans:
                ans = arr[k][n][m]
        if flag:
            break
    if flag:
        print(-1)
        break

if not flag and ans == 1:
    print(0)
elif not flag:
    print(ans-1)
'''





