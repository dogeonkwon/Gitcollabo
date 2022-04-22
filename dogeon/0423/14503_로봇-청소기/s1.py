# 14503_로봇-청소기 풀이
# 2022-04-23


def clean(r, c, d):
    global cnt, stop

    if stop:        # 종료조건
        return

    if not visited[r][c]:   # 청소한 적이 없다면 청소해주고 횟수+1
        visited[r][c] = 1
        cnt += 1
    conti = 0       # 연속 4번 일 경우의 갯수 파악
    for k in ((d+3) % 4, (d+2) % 4, (d+1) % 4, d):  # 들어온 방향의 시계반대방향으로 탐색
        nr = r + direct[k][0]
        nc = c + direct[k][1]
        conti += 1
        if stop:
            return
        elif not arr[nr][nc] and not visited[nr][nc]:   # 빈 칸이고 청소한 적이 없다면 clean으로 넘어가기
            clean(nr, nc, k)
        elif conti == 4:                # 연속 4번 됐다면 조건을 보고 후진시켜주기(스택이 아니라 후진임!)
            br = r + direct[(d+2) % 4][0]       # 들어온 방향의 반대방향
            bc = c + direct[(d+2) % 4][1]
            if arr[br][bc]:     # 벽이라면 그냥 종료
                stop = 1
                return
            else:               # 아니라면 후진시켜주기(방향은 들어온 방향 그대로)
                clean(br, bc, d)


direct = [(-1, 0), (0, 1), (1, 0), (0, -1)]     # 델타탐색

N, M = map(int, input().split())
rr, cc, dd = map(int, input().split())      # 로봇청소기가 있는 칸의 좌표(rr, cc)와 방향(dd)
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]      # 청소한 칸 표시
cnt = stop = 0      # 청소하는 칸, 종료조건(1이 되면 종료)
clean(rr, cc, dd)     # 로봇청소기 작동!
print(cnt)