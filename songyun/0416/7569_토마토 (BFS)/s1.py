import sys
sys.stdin = open('input.txt')

def BFS():
    global cnt, box

    # 하, 상, 뒤, 앞, 우, 좌
    dh = (1, -1, 0, 0, 0, 0)
    dr = (0, 0, 1, -1, 0, 0)
    dc = (0, 0, 0, 0, 1, -1)

    queue = []
    # 1이 있는 토마토의 위치를 찾고 그 좌표를 queue 에 넣는다.
    for h in range(H):          # 층
        for r in range(N):      # 행
            for c in range(M):  # 열
                if box[h][r][c] == 1:
                    queue.append([h, r, c])
    while queue:
        v = queue.pop(0)
        # [0, 1, 3]
        # [0, 1, 4]
        # [0, 2, 3]
        # [0, 2, 4]

        for k in range(6):
            nh = v[0] + dh[k]
            nr = v[1] + dr[k]
            nc = v[2] + dc[k]

            if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M and box[nh][nr][nc] == 0:
                box[nh][nr][nc] = 1
                cnt[nh][nr][nc] = cnt[v[0]][v[1]][v[2]] + 1
                queue.append((nh, nr, nc))
    print(cnt)

def check(box):
    # 이미 다 익은 상태 인지 확인
    for h in range(H):  # 층
        for r in range(N):  # 행
            for c in range(M):  # 열
                if box[h][r][c] == 0:
                    return -1
    return 0

# M : 열, N : 행 , H : 층
M, N, H = list(map(int, input().split()))

box = list(list(list(map(int,input().split())) for _ in range(N)) for _ in range(H))

# 해당자리의 토마토가 며칠만에 익었는지 계산할 리스트
cnt = [[[0]*M for _ in range(N)] for _ in range(H)]


# 만약 이미 다 익은 상태라면 0을 출력
if check(box) == 0:
    print(0)


# 익지 않은 사과가 하나라도 있다면 지켜본다.
elif check(box) == -1:
    BFS()
    # 지켜 본 결과 덜 익은 사과가 아직 있다면 -1을 출력
    if check(box) == -1:
        print(-1)

    # 사과가 모두 익었다면, 익는데 최대 며칠이 걸렸는지 출력한다.
    else:
        ans = 0
        for h in range(H):  # 층
            for r in range(N):  # 행
                for c in range(M):  # 열
                    if cnt[h][r][c] > ans:
                        ans = cnt[h][r][c]
        print(ans)






# import sys
# sys.stdin = open('input.txt')
#
# T = int(input())
#
# for tc in range(1, T+1):
#     M, N, H = list(map(int, input().split()))
#
#     box = [list(map(int, input().split())) for _ in range(N*H)]
#
#     cnt_f = 0
#     ans = 1
#     while True:
#
#         # 모든 토마토가 이미 다 익은 경우 (0이 있는지 확인)
#         for i in range(N*H):
#             for j in range(M):
#                 if box[i][j] == 0:
#                     cnt_f += 1
#
#                 if cnt_f >= 1:
#                     break
#             if cnt_f >= 1:
#                 break
#
#         if cnt_f == 0:
#             ans = 0
#             break
#
#         else:
#             break
#
#     print(ans)
