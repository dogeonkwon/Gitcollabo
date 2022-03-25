# 4881_배열-최소-합 풀이
# 2022-02-24

import sys
sys.stdin = open('sample_input.txt', 'r')


def dfs(r, ssum, visited):   # 행의 인덱스 / 합계 / 방문여부
    global ans
    if ssum >= ans:         # 가지치기 - 최소값을 찾는 문제이므로 r이 N만큼 되기전에 ssum이 ans보다 커진다면 종료시켜도 된다.
        return

    if r >= N:              # r이 N만큼 되었다면 ssum이 ans보다 작다면 교체
        if ssum < ans:
            ans = ssum
        return

    for i in range(N):          # arr의 행을 탐색
        if not visited[i]:      # 방문 한 적이 없는 열이라면
            visited[i] = True   # 방문 표시를 해주고
            dfs(r+1, ssum+arr[r][i], visited)      # 다음 행으로 넘어갈 수 있도록 한다.
            visited[i] = False      # dfs에서 나왔다면 True를 없애줘야 다른 경우의 수를 확인해 볼 수 있다.


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 99                    # 비교할 최소값
    visited = [False] * N       # 방문여부
    dfs(0, 0, visited)

    print('#{} {}'.format(tc, ans))