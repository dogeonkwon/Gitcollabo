import sys

sys.stdin = open('input.txt')


def dfs(r, c, d):
    global ans

    # 1. 현재 위치가 0 이면 청소 한다.
    if room[r][c] == 0:
        room[r][c] = 2
        ans += 1

    # 2. 빙빙 돌면서 청소할 곳 탐색
    # 처음 바라보는 방향이 0(북) 이면
    # 3(서) -> 2(남) -> 1(동) 순으로 돈다.
    turn = d
    for k in range(4):

        turn = (turn + 3) % 4

        nr = r + delta[turn][0]
        nc = c + delta[turn][1]

        # 도는 중에 청소할 곳이 있다면
        if 0 <= nr < N - 1 and 0 <= nc < M - 1:
            if room[nr][nc] == 0:
                # 그곳에 가서 1번 반복
                # print('{} {}가 호출'.format(nr,nc))
                dfs(nr, nc, turn)
                # print('{} {}가 리턴'.format(nr,nc))
                return

    # 더 이상 청소할 곳이 없다면 후진
    nr = r - delta[turn][0]
    nc = c - delta[turn][1]

    # 후진한 곳이 벽이 아니라면 다시 탐색
    if room[nr][nc] != 1:
        dfs(nr, nc, turn)

    ## 밑에 else 구문 없어도 답이 나오던데 왜 그런걸까...
    else:
        # print('벽발견 {} {}에서 리턴'.format(nr, nc))
        return


N, M = list(map(int, input().split()))

# d = 0(북), 1(동), 2(남), 3(서)
r, c, d = list(map(int, input().split()))
room = [list(map(int, input().split())) for _ in range(N)]


delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]

ans = 0

dfs(r, c, d)

print(ans)
