import sys
sys.stdin = open('input.txt', 'r')

# 최단거리 구하기
def bfs(start):
    queue = []
    front = -1
    rear = -1
    queue.append(start)
    rear += 1

    while front != rear:
        front += 1
        start = queue[front]

        oi = start[0]
        oj = start[1]
        # 델타 탐색
        for di, dj in [[-1, 0], [1, 0],[0, 1],[0, -1]]:
            ni = oi + di
            nj = oj + dj
            if ni < 0 or ni >= N or nj <0 or nj >= M:
                continue
            #distance 구하기
            if arr[ni][nj] == 1:
                queue.append([ni, nj])
                rear+=1
                arr[ni][nj] = arr[oi][oj] +1
    return (arr[N-1][M-1])

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0]* M for _ in range(N)]
# bfs 돌리기
print(bfs([0,0]))
