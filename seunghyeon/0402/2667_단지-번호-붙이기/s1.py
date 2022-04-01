# 2667_단지 번호 붙이기 풀기
# 2022-03-31


def dfs(i, j):
    global arr, cnt
    arr[i][j] = 0

    # 델타 탐색
    for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        ci = i + di
        cj = j + dj

        # 집이 있으면
        if 0 <= ci < N and 0 <= cj < N and arr[ci][cj]:
            cnt += 1          # 단지 넓히기
            arr[i][j] = 0     # 방문 표시
            dfs(ci, cj)       # 더 깊이 들어가기 !
    return


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
result = list()

for n in range(N):
    for m in range(N):
        # 단지 찾기
        if arr[n][m]:
            cnt = 1
            dfs(n, m)
            result.append(cnt)

result.sort()        # 단지를 크기 순으로 정렬
print(len(result))   # 단지 수
for r in result:
    print(r)

