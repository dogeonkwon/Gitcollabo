# 2178_미로탐색 풀이
# 2022-03-14

N, M = map(int, input().split())
miro = [list(map(int, input())) for _ in range(N)]
miro[0][0] = 0       # 출발지 초기화
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]   # 델타 탐색
queue = [[[0, 0]]]   # 초기 queue
cnt = 1
stop = 0

# queue가 빌 때까지 반복
while queue:
    start = queue.pop(0)  # 시작위치 받아오기
    cnt += 1              # 카운팅 +1
    v = list()            # bfs 같은 선상을 같이 담아서 queue에 저장

    for s in start:       # n번째일 때
        ci = s[0]         # 행
        cj = s[1]         # 열

        # 상하좌우탐색
        for di, dj in delta:
            ni = ci + di
            nj = cj + dj

            # 인덱스 에러 방지
            if 0 <= ni < N and 0 <= nj < M:

                # 갈 수 있으면(1), 지나갔으므로 0으로 바꾸고 v에 좌표추가
                if miro[ni][nj] == 1:
                    miro[ni][nj] = 0
                    v.append([ni, nj])

                # 도착하면 멈춤
                if ni == N-1 and nj == M-1:
                    stop = 1
                    break
        if stop == 1:
            break
    if stop == 1:
        break
    # 도착하지 않았을 경우, queue에 경로 추가 후 반복
    else:
        queue.append(v)

print(cnt)