import sys
sys.stdin = open('input.txt','r')

def bfs(i,j):
    queue = [[i,j]]
    visited[i][j] =1
    while queue:
        start = queue.pop(0)
        s_i, s_j = start[0], start[1]
        for di, dj in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            ni, nj = s_i + di, s_j +dj
            if 0<= ni< N and 0<= nj < N and visited[ni][nj] ==0 and arr2[ni][nj]==0:
                queue.append([ni,nj])
                visited[ni][nj] =1


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

min_height = arr[0][0]
max_height = arr[0][0]
for i in range(N):
    for j in range(N):
        if arr[i][j] > max_height:
            max_height = arr[i][j]
        if arr[i][j] < min_height:
            min_height = arr[i][j]

area_list = [1]
if min_height == 0 and max_height == 0:
    print(1)
else:
    height = min_height
    while height <= max_height:
        arr2 = [[0]* N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if arr[i][j] <= height:
                    arr2[i][j] =1

        visited = [[0] * N for _ in range(N)]
        idx = 0
        for i in range(N):
            for j in range(N):
                if arr2[i][j] == 0 and visited[i][j] == 0:
                    bfs(i,j)
                    idx +=1
        area_list.append(idx)
        height+=1
    print(max(area_list))