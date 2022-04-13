# 7569_토마토
# 2022-04-12


def bfs(queue, front, rear):
    global result, val

    while front < rear-1:
        front += 1
        h, n, m = queue[front]

        # 3차원 델타 탐색
        for dh, dm, dn in (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, -1), (0, 0, 1):
            ch, cm, cn = h + dh, m + dm, n + dn

            if 0 <= ch < H and 0 <= cm < M and 0 <= cn < N:
                # 토마토가 안익었으면
                if tomatoes[ch][cn][cm] == 0:
                    tomatoes[ch][cn][cm] = tomatoes[h][n][m] + 1  # 익힘 표시
                    result += 1                                   # 익은 토마토 추가
                    queue.append((ch, cn, cm))
                    rear += 1

                # 토마토가 익었으면
                elif tomatoes[ch][cn][cm] == 1:
                    # 더 빠르게 익을 수 있는 기간으로 익히기
                    tomatoes[ch][cn][cm] = tomatoes[h][n][m] + 1 if tomatoes[h][n][m] + 1 < tomatoes[ch][cn][cm] else tomatoes[ch][cn][cm]

                # 마지막 토마토가 익을 때까지의 경과일
                if tomatoes[ch][cn][cm] > val:
                    val = tomatoes[ch][cn][cm]

            # 토마토가 다 익으면 끝 !
            if result == cnt:
                return


M, N, H = map(int, input().split())
tomatoes = [[] for _ in range(H)]
cnt = M*N*H       # 토마토의 총 개수
result = 0        # 익은 토마토 수
val = 0           # 토마토가 다 익는 기간
queue = list()    # queue
front = -1        # queue의 front
rear = 0          # queue의 rear

# 3차원 배열만들기
for k in range(N*H):
    v = list(map(int, input().split()))
    for p in range(M):
        if v[p] == 1:
            result += 1
            queue.append((k//N, k%N, p))
            rear += 1
        if v[p] == -1:
            cnt -= 1
    tomatoes[k//N].append(v)

# 토마토가 이미 다익었을 경우
if result == cnt:
    print(0)
# 그렇지 않은 경우
else:
    bfs(queue, front, rear)
    # 익지 못하는 토마토가 존재하면 -1
    if cnt != result:
        print(-1)
    else:
        print(val-1)

