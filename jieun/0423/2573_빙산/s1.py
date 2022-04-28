import sys
sys.stdin = open('input.txt','r')

# from collections import deque

sys.setrecursionlimit(10000)
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 옆이 2라서 옆 에 빙산에 영향을 줄 경우 고려 x
def ice_melt(i, j):
    global zero
    for d in range(4):
        if 0<= i+di[d] < N and 0<= j+dj[d] < M and arr[i+di[d]][j+dj[d]]==0:
            zero +=1
    # 빙산 높이가 주변의 0의 개수보다 클 때
    arr[i][j] = max(arr[i][j]-zero, 0)


def dfs(i, j):
    global land_count
    visited[i][j] =1
    for d in range(4):
        ni, nj = i+di[d], j+dj[d]
        if 0<= ni< N and 0<= nj <M and arr[ni][nj] > 0 and visited[ni][nj]==0:
            visited[ni][nj] =1
            land_count +=1
            dfs(ni,nj)

# def bfs(i, j):
#     queue = deque()
#     queue.append([i,j])
#     visited[i][j] =1
#     while queue:
#         start = queue.popleft()
#         s_i = start[0]
#         s_j = start[1]
#         for di, dj in [[-1,0],[1,0],[0, -1], [0,1]]:
#             ni, nj = s_i+di, s_j +dj
#             if 0<= ni< N and 0<= nj <M and arr[ni][nj] > 0 and visited[ni][nj]==0:
#                 visited[ni][nj]=1
#                 queue.append([ni, nj])
di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]

# 전부 다 녹았는지 확인하기 위해 남아있는 빙산의 개수 세주기
land_count = 1
# 몇년이 지났을까
year = 0
# 덩어리 개수
cnt = 0

#덩이리 개수가 2개 미만일 경우와 빙산이 남아있을 때만 해주기
while cnt < 2 and land_count >0:
    land_count =0
    cnt =0
    visited = [[0]* M for _ in range(N)]
    
    # 땅덩어리 탐색
    for n in range(N):
        for m in range(M):
            if arr [n][m] >= 1 and visited[n][m] ==0:
                dfs(n, m)
                cnt +=1

    if cnt >=2:
        break
    
    # 아직 빙산이 한덩어리 뿐!
    for i in range(N):
        for j in range(M):
            if arr[i][j] >0:
                # 주변 0의 개수
                zero = 0
                # 녹여버려
                ice_melt(i, j)
    year += 1


if cnt <2 :
    print(0)
else:
    print(year)