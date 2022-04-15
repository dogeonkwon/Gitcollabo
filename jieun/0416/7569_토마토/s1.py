from collections import deque

import sys
sys.stdin = open('input.txt','r')


def bfs(k, i, j):
    queue = deque()
    queue.append([k, i,j])
    visited[k][i][j]=1
    while queue:
        start = queue.popleft()
        s_k = start[0]
        s_i = start[1]
        s_j = start[2]
        # 6방향으로 돌려차기!
        for dk, di, dj in [[0, 0, 1],[0, 0, -1], [0, 1,0], [0, -1,0], [-1, 0, 0],[1, 0, 0]]:
            ni, nj,nk  = s_i+di, s_j + dj, s_k + dk
            if 0<=ni< N and 0<= nj <M and 0<= nk < H and visited[nk][ni][nj] == 0:
                # 익지 않은 토마토
                if arr[nk][ni][nj] == 0:
                    arr[nk][ni][nj] =1
                    queue.append([nk, ni,nj])
                    visited[nk][ni][nj] = visited[s_k][s_i][s_j] +1


# 테스트 케이스
T = int(input())
for t in range(1, T+1):
    # 가로 세로 높이
    M, N, H = map(int, input().split())
    arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
    
    # 방문 및 거리 처리
    visited = [[[0]*M for _ in range(N)] for _ in range(H)]
    # 익은 토마토만 처리해줄거야!
    for k in range(H):
        for i in range(N):
            for j in range(M):
                if arr[k][i][j] == 1:
                    bfs(k, i,j)
    
    # 최대 거리 계산하기
    max_value = visited[0][0][0]
    zero = 1
    for k in range(H):
        if zero == 0:
            break    
        for i in range(N):
            if zero == 0:
                break
            for j in range(M):
                if arr[k][i][j] == 0:
                    zero = 0
                    max_value = -1
                    break
                if visited[k][i][j] > max_value:
                    max_value = visited[k][i][j]
    
    # 익지 않은 토마토가 아직도 안익엇다? 그러면 -1
    if max_value == -1:
        print(-1)
    # 처음을 1로 시작했으니까 거리는 -1 해줘야함
    else:
        print(max_value -1)
