# 5014_스타트링크 풀이
# 2022-04-16


def bfs_U(s, cnt):      # 출발지 < 도착지 일 경우 선택하는 bfs
    front = -1
    rear = 0
    q = [[s, cnt]]
    while front < rear:
        front += 1
        v = q[front][0]
        c = q[front][1]
        if floor[G]:            # 방문 층이 0이 아니라면 방문했다는 의미이므로 stop!
            return
        if v + U <= F and not floor[v+U]:   # U만큼 올라갔을 때 최고 층보다 낮고 방문한 적이 없다면
            floor[v+U] = c
            q.append([v+U, c+1])
            rear += 1
        if v - D > 0 and not floor[v-D]:    # D만큼 내려갔을 때 최소 층보다 높고 방문한 적이 없다면
            floor[v-D] = c
            q.append([v-D, c+1])
            rear += 1


def bfs_D(s, cnt):      # 출발지 > 도착지 일 경우 선택하는 bfs
    front = -1
    rear = 0
    q = [[s, cnt]]
    while front < rear:
        front += 1
        v = q[front][0]
        c = q[front][1]
        if floor[G]:
            return
        if v - D > 0 and not floor[v-D]:
            floor[v-D] = c
            q.append([v-D, c+1])
            rear += 1
        if v + U <= F and not floor[v+U]:
            floor[v+U] = c
            q.append([v+U, c+1])
            rear += 1


F, S, G, U, D = map(int, input().split())   # F : 최대 층 / S : 현재 위치 / G : 목적지 / U : 올라갈 수 있는 층수 / D : 내려갈 수 있는 층수
floor = [0] * (F+1)
floor[S] = 1

if S < G and U:     # 출발지 < 도착지 일 경우 선택하는 bfs
    bfs_U(S, 1)
elif S > G and D:   # 출발지 > 도착지 일 경우 선택하는 bfs
    bfs_D(S, 1)

if S == G:      # 시작과 도착 층수가 같다면 0
    print(0)
elif floor[G]:  # 다르다면 방문 층에 저장된 숫자 출력
    print(floor[G])
else:       # 방문한 적이 없다면 문자열 출력
    print('use the stairs')