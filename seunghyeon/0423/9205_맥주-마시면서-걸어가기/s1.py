# 9205_맥주 마시면서 걸어가기
# 2022-04-21

'''
틀렸습니다 !
왜일까? 과연 최대로 이동가능한 거리로 가야할까?
사실은 편의점으로 갈 수 있는 길만 찾아도 된다 !
그럼 가장 짧은 거리로 갈 수 있는 길을 찾아보자 !
'''


def func(v):
    beers = 20
    cnt = 0
    visited[v] = 1

    while cnt < N+2:
        # 갈 수 있는 가장 가까운 먼 거리 구하기
        can_go = beers * 50

        # 만일 도착지점이 이동거리내에 있으면 도착 !
        if graph[v][N+1] <= can_go:
            return print('happy')

        idx = -1
        val = 70000
        for i in range(N+2):
            # 방문한 적 없고, 이동 가능한 거리내에서
            if not visited[i] and graph[v][i] <= can_go:
                # 최대로 이동가능한 거리 찾기
                if can_go-graph[v][i] < val:
                    idx = i
                    val = can_go-graph[v][i]

        # 이동못하면 끝 ㅠㅠ
        if idx < 0:
            return print('sad')

        visited[idx] = 1
        v = idx
        cnt += 1


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

    func(0)