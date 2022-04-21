# 9205_맥주 마시면서 걸어가기
# 2022-04-21


def bfs():
    visit = [False] * (N + 2)
    queue = [0]
    front = -1
    rear = 0
    can_go = 1000

    while front < rear:
        front += 1
        start = queue[front]
        visit[start] = True

        # 페스티벌에 도착할 수 있어 !
        if graph[start][N+1] <= can_go:
            return print('happy')

        for i in range(N+2):
            # 방문한 적 없고, 이동 가능한 거리내에 있으면 탐색해줘 !
            if not visit[i] and graph[start][i] <= can_go:
                visit[i] = True
                queue.append(i)
                rear += 1
    
    # 페스티벌에 어떻게 가도 도착 못해 ㅜㅜ
    return print('sad')


T = int(input())
for _ in range(T):
    N = int(input())
    spots = [list(map(int, input().split())) for _ in range(N+2)]
    graph = [[0]*(N+2) for _ in range(N+2)]
    visited = [0] * (N + 2)

    # 그래프 만들기 (0번에서 N+1번에 도착하기 !)
    for n in range(N+2):
        for m in range(n+1, N+2):
            v = abs(spots[n][0] - spots[m][0]) + abs(spots[n][1] - spots[m][1])
            graph[n][m] = v
            graph[m][n] = v

    bfs()