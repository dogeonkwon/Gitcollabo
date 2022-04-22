# 14503_로봇청소기
# 2022-04-21

N, M = map(int, input().split())      # N: 행, M: 열
r, c, d = map(int, input().split())   # 로봇청소기의 좌표 (r, c) / 로봇청소기의 방향 d
arr = [list(map(int, input().split())) for _ in range(N)]
directions = ((-1, 0), (0, 1), (1, 0), (0, -1))  # 북동남서(상우하좌)
cnt = 1             # 로봇청소기가 청소한 방
arr[r][c] = 2       # 청소표시

# 빈 방의 개수 구하기
rooms = 1
for n in range(N):
    for m in range(M):
        if not arr[n][m]:
            rooms += 1

while True:
    check = 0        # 청소여부확인

    for n in range(4):
        dd = (d + 3) % 4         # 현재 바라보는 곳의 왼쪽 방향
        nr, nc = r + directions[dd][0], c + directions[dd][1]       # 왼쪽의 좌표

        if 0 <= nr < N and 0 <= nc < M:       # 인덱스 범위 내에 있으면
            # 청소한 적 없으면 청소한다 !
            if not arr[nr][nc]:
                d = dd
                r, c = nr, nc
                cnt += 1
                arr[r][c] = 2

                # 빈방을 모두 청소하면 청소 끝 - !
                if rooms == cnt:
                    break
                check = 1
                break
            else:
                d = dd  # 방향전환

                # 만약 4번을 방향전환했는데 청소할 곳이 없으면 뒤를 확인한다 !
                if n == 3:
                    dd = (d + 2) % 4
                    nr, nc = r + directions[dd][0], c + directions[dd][1]

                    # 벽이 아니라면 후진 !
                    if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != 1:
                        r, c = nr, nc
                        check = 1
                        break

    if check:
        continue
    else:
        break

print(cnt)
