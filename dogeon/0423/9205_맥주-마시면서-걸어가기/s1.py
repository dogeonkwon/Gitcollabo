# 9205_맥주-마시면서-걸어가기 풀이
# 2022-04-23


def bfs(x, y):

    front = -1
    rear = 0
    q = [[x, y]]

    while front < rear:
        front += 1
        vx = q[front][0]
        vy = q[front][1]

        for k in range(n+2):    # 출발지로 바로 갈 수도 있으므로 앞에서부터 탐색(순서는 딱히 상관없을듯)
            if abs(distance[k][0] - vx) + abs(distance[k][1] - vy) <= 1000 and not visited[k]:  # 거리가 맥주 20병을 마실 동안 갈 수 있는 거리이며 방문한 적이 없다면
                q.append([distance[k][0], distance[k][1]])
                visited[k] = 1
                rear += 1


T = int(input())
for _ in range(T):
    n = int(input())
    distance = [[0] for _ in range(n+2)]    # 출발지, 편의점, 목적지의 집합
    visited = [0] * (n+2)       # 방문 체크
    result = 1      # 결과값

    for l in range(n+2):    # 위치들을 받아주고
        i, j = map(int, input().split())
        distance[l] = [i, j]

    visited[-1] = 1     # 도착지에서 출발지까지 갈 수 있는지 탐색하기 위해 도착지 먼저 체크해둠
    bfs(distance[-1][0], distance[-1][1])

    if visited[0] and visited[-1]:  # 출발지와 목적지 둘 다 방문처리가 되었다면
        print('happy')
    else:
        print('sad')