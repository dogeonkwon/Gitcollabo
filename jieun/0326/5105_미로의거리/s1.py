import sys
sys.stdin = open('input.txt','r')

def bfs(i, j):
    global distance, ans

    while queue:
        start = queue.pop(0)
        oi = start[0]
        oj = start[1]
        for di, dj in [[-1,0],[1,0],[0,1],[0,-1]]:
            ni = oi+di
            nj = oj+dj
            if 0<= ni< N and 0<= nj < N and arr[ni][nj] != 1 and [ni,nj] not in visited:
                queue.append([ni,nj])
                visited.append([ni,nj])
                distance[ni][nj] = distance[oi][oj] +1
                if arr[ni][nj] == 3:
                    ans = distance[ni][nj] -1
                    return


T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    
    distance = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start_i = i
                start_j = j
                break
    visited = [[start_i,start_j]]
    ans = 0
    queue = [[start_i, start_j]]
    bfs(start_i, start_j)
    print('#{} {}'.format(t, ans))
