# 17070_파이프-옮기기1 풀이
# 2022-04-04


def dfs(i, j, visited):
    global cnt, home

    if i == N-1 and j == N-1:
        cnt += 1
        return

    if visited == 2:     # 가로일 때
        if 0 <= j + 1 < N and not home[i][j+1]:  # 가로로 갈 수 있으면 가줘 !
            if j < N - 2 or i == N - 1:
                dfs(i, j+1, 2)

            if 0 <= i + 1 < N and not home[i+1][j] and not home[i+1][j+1]:  # 대각선으로 갈 수 있으면 가줘 !
                dfs(i + 1, j + 1, 4)

    if visited == 3:     # 세로일 때
        if 0 <= i + 1 < N and not home[i+1][j]:  # 세로로 갈 수 있으면 가줘 !
            if i < N - 2 or j == N - 1:
                dfs(i+1, j, 3)

            if 0 <= j + 1 < N and not home[i][j+1] and not home[i+1][j+1]:  # 대각선으로 갈 수 있으면 가줘 !
                dfs(i + 1, j + 1, 4)

    if visited == 4:      # 대각선일 때
        if i < N - 2 or j == N - 1:  # 세로로 갈 수 있으면 가줘 !
            if 0 <= i + 1 < N and not home[i + 1][j]:
                dfs(i + 1, j, 3)

        if j < N - 2 or i == N - 1:  # 가로로 갈 수 있으면 가줘 !
            if 0 <= j + 1 < N and not home[i][j + 1]:
                dfs(i, j + 1, 2)

        if 0 <= i + 1 < N and 0 <= j + 1 < N:  # 대각선으로 갈 수 있으면 가줘 !
            if not home[i + 1][j] and not home[i][j + 1] and not home[i + 1][j + 1]:
                dfs(i + 1, j + 1, 4)


N = int(input())
home = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
dfs(0, 1, 2)
print(cnt)

