import sys
sys.stdin = open('input.txt','r')


def making_graph(arr):
    for i in range(N+2):
        for j in range(N+2):
            if i != j and abs(arr[i][0]-arr[j][0])+abs(arr[i][1]-arr[j][1]) <= 1000:
                graph[i].append(j)
                graph[j].append(i)

def dfs(start):
    visited[start] = 1
    for next in graph[start]:
        if visited[next]==0:
            visited[next]=1
            dfs(next)


T = int(input())
for t in range(1, T+1):
    N= int(input())
    arr = [list(map(int, input().split())) for _ in range(N+2)]
    graph = [[] for _ in range(N+2)]
    visited = [0] * (N+2)
    making_graph(arr)
    dfs(0)
    if visited[-1] ==1:
        print('happy')
    else:
        print('sad')


# 왜 안되지 빠꾸빠꾸
# def dfs(i,j):
#     visited.append([i,j])
#     if i== arr[N+1][0] and j == arr[N+1][1]:
#         return
#     for c in range(1, N+2):
#         if (abs(i-arr[c][0]) + abs(i-arr[c][1])) <=1000 and [arr[c][0], arr[c][1]] not in visited:
#             dfs(arr[c][0], arr[c][1])


# T = int(input())
# for t in range(1, T+1):
#     N= int(input())
#     arr = [list(map(int, input().split())) for _ in range(N+2)]
    
#     visited = []
#     dfs(arr[0][0], arr[0][1])
#     print(visited)
#     if [arr[N+1][0], arr[N+1][1]] in visited:
#         print('happy')
#     else:
#         print('sad')