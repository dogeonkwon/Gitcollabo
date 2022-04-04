# 2667_단지번호-붙이기 풀이
# 2022-04-05

import sys
sys.stdin = open('input.txt', 'r')


def attach(r, c):           # 행과 열의 좌표를 받아옴
    front = -1
    rear = 0
    q = [(r, c)]            # q에 첫 행과 열의 좌표를 넣어주고 그 지점을 cnt로 바꿔준다.
    arr[r][c] = cnt
    lst.append(cnt)         # lst에 cnt 추가

    while front != rear:
        front += 1
        v = q[front]
        for dr, dc in (0, 1), (1, 0), (0, -1), (-1, 0):         # 델타탐색
            nr = v[0] + dr
            nc = v[1] + dc
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 1:        # 탐색을 한 좌표가 배열범위 안에 있고 1이라면
                arr[nr][nc] = cnt                 # arr을 cnt로 바꿔주고
                q.append((nr, nc))                # q에 넣어준다.
                lst.append(cnt)                   # lst에 cnt도 추가
                rear += 1                         # rear 1추가


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
cnt = 1                         # 아파트 단지의 개수를 기록하기 위한 변수(기존 배열이 0, 1로 이루어져 있기 때문에 cnt를 1부터 시작)
lst = list()                 # 각 단지들이 보유하고 있는 아파트 개수를 저장하기 위한 변수
result = list()

for i in range(N):              # 전 범위 탐색
    for j in range(N):
        if arr[i][j] == 1:      # 1인 곳이 있다면 아파트 단지가 될 수 있으므로 cnt를 1 더해주고 attach 함수에 행, 열 좌표를 넣어준다.
            cnt += 1
            attach(i, j)
print(cnt-1)                   # 단지 탐색이 다 끝났다면 cnt-1을 하여 단지 종류를 출력

while cnt != 1:
    sub = 0
    for n in lst:               # 저장된 단지번호를 같은 번호끼리 개수를 확인
        if n == cnt:
            sub += 1
    result.append(sub)
    cnt -= 1

result.sort()                   # result를 오름차순 정렬하여
for l in range(len(result)):    # 하나씩 출력
    print(result[l])