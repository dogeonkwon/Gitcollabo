# 5014_스타트링크
# 2022-04-13


def bfs(v):
    floors[v] = 1
    queue = [v]
    front = -1
    rear = 0

    while front < rear:
        front += 1
        s = queue[front]
        
        for p in (U, -D):   # +U, -D
            
            # 만일 1~F층 사이에 있고, 방문한 적이 없으면
            if 0 < s+p < F+1 and not floors[s+p]:
                floors[s+p] = floors[s] + 1   # 누적합
                
                # G에 도달하면 return !
                if s+p == G:
                    return
                
                queue.append(s+p)
                rear += 1


# F: 최고층, S: 시작 위치, G: 스타트링크 위치, U: +U, D: -D
F, S, G, U, D = map(int, input().split())
floors = [0] * (F+1)
bfs(S)

if floors[G]:   # 도착할 수 있는 경우
    print(floors[G]-1)
else:           # 도착할 수 없는 경우
    print('use the stairs')