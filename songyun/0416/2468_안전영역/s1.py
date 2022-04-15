import sys
sys.stdin = open('input.txt')

def dfs(y, x, r):
    # 현재 위치를 방문 처리하고
    visited[y][x] = True

    # 델타 탐색, (상 하 좌 우)
    for i in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ny = y + i[0]
        nx = x + i[1]
        # 범위 안에 들어오고
        if 0 <= ny < N and 0 <= nx < N:
            # 강수량 보다 높은 곳이고 방문 하지 않았다면
            if area[ny][nx] > r and not visited[ny][nx]:
                # 인접 지역 탐색
                dfs(ny, nx,r)


area = []
result = 1
MAX = 0
N = int(input())


# input
for _ in range(N):
    row = list(map(int, input().split()))
    mmax = max(row)

    if mmax > MAX:
        MAX = mmax
    area.append(row)


# 강수량의 변화는 1부터 제일 높은 지역-1 까지 봐야 한다 .
for i in range(1, MAX):

    # 강수량이 바뀔 때 마다 visited 와 cnt 를 초기화 한다
    visited = [[False]*N for _ in range(N)]
    cnt = 0

    # BFS
    for j in range(N):
        for k in range(N):

            # 만약 탐색 지역이 강수량 보다 높은 지역이고, 방문하지 않았다면
            if area[j][k] > i and not visited[j][k]:
                # 탐색 시작
                dfs(j, k, i)
                # dfs 가 끝나면 cnt+1을 한다.
                cnt += 1

    # 만약 cnt 가 result 보다 크다면 갱신한다.
    if cnt > result:
        result = cnt

print(result)