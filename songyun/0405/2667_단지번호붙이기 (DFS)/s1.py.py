import sys
sys.stdin = open('input.txt')

def DFS(s):
    global arr, cnt

    # 현재 좌표 넣기
    r = s[0]
    c = s[1]

    # 현재 좌표 0으로 바꾸기
    arr[r][c] = 0

    # 델타 탐색
    for k in ((-1, 0), (0, 1), (1, 0), (0, -1)):      # 상우하좌
        nr = r + k[0]
        nc = c + k[1]

        # 새로운 좌표가 범위안에 들어오고, 1 이라면 이동한다.
        if 0 <= nr < N and 0 <= nc < N:
            if arr[nr][nc] == 1:
                arr[nr][nc] = 0
                cnt += 1
                DFS([nr, nc])



N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
ans = []

# 시작 좌표를 포함해서 갯수를 세기 때문에 1로 시작

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            # 새로운 단지를 찾을 때 마다 cnt=1 로 초기화
            cnt = 1
            DFS([i, j])
            # 단지내 세대수를 ans 에 append 한다.
            ans.append(cnt)


print(len(ans))
ans.sort()
for i in ans:
    print(i)



