# 17135_캐슬-디펜스 풀이
# 2022-04-09

def pick(n, picked, topick):
    global archer, cnt_archer

    if topick == 0:
        archer += [picked[:]]
        cnt_archer += 1
        return

    if not picked:
        smallest = 0
    else:
        smallest = picked[-1]
    for i in range(smallest, n):
        if i not in picked:
            picked.append(i)
            pick(n, picked, topick-1)
            picked.pop()


N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
enemy = list()    # 적의 위치
cnt_enemy = 0     # 적의 수

archer = list()     # 궁수의 위치 조합
cnt_archer = 0      # 궁수 위치 조합 수

pick(M, [], 3)      # 궁수 위치의 조합해주는 함수
ans = 0     # 정답!

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            enemy += [[i, j, 0]]    # 행과 열의 좌표, 화살에 맞았다면 상태를 바꿔주기 위한 0
            cnt_enemy += 1

for arc in range(cnt_archer):   # 궁수 배치!
    end = 0         # 범위 밖으로 나가거나 궁수에게 잡힌 적의 수
    sub = 0         # 궁수에게 잡힌 적의 수
    forward = 0     # 적들이 얼마나 전진했는지

    while end < cnt_enemy:  # 잡을 수 있는 최대 적 조회!
        target = set()      # 한 턴에 잡은 적의 중복을 피하기 위해 set

        aa = 99             # 거리(최소거리를 구하기 위해)
        bb = 99
        cc = 99

        a_target = -1       # 잡은 적의 인덱스 번호 저장
        b_target = -1
        c_target = -1

        for d in range(cnt_enemy-1, -1, -1):
            if enemy[d][2] == arc:
                if enemy[d][0] + forward >= N-1:    # 범위 밖으로 나갔을 때
                    enemy[d][2] += 1                # 표시를 해줌
                    end += 1        # end를 1 더해줌

                a_len = abs(N-(enemy[d][0] + forward)) + abs(archer[arc][0]-enemy[d][1])    # 거리 구하기
                b_len = abs(N-(enemy[d][0] + forward)) + abs(archer[arc][1]-enemy[d][1])
                c_len = abs(N-(enemy[d][0] + forward)) + abs(archer[arc][2]-enemy[d][1])

                if a_len <= D:   # a궁수에게 걸리는 적 체크
                    if a_len < aa:      # 이 전에 적의 거리보다 짧다면 바로 갱신
                        a_target = d
                        aa = a_len
                    elif a_len == aa:       # 같다면 왼쪽에 있는 값인지 비교
                        if enemy[d][1] <= enemy[a_target][1]:
                            a_target = d

                if b_len <= D:   # b궁수에게 걸리는 적 체크
                    if b_len < bb:
                        b_target = d
                        bb = b_len
                    elif b_len == bb:
                        if enemy[d][1] <= enemy[b_target][1]:
                            b_target = d

                if c_len <= D:   # c궁수에게 걸리는 적 체크
                    if c_len < cc:
                        c_target = d
                        cc = c_len
                    elif c_len == cc:
                        if enemy[d][1] <= enemy[b_target][1]:
                            c_target = d

        if a_target != -1:          # 한 바퀴 돌고 난 뒤 target에 넣어주기
            target.add(a_target)
        if b_target != -1:
            target.add(b_target)
        if c_target != -1:
            target.add(c_target)

        if target:              # target에 새로운 값들이 생겼다면 잡은 표시(enemy[t][2] += 1)을 해주고 end를 1 더해준다
            for t in target:
                sub += 1
                if enemy[t][2] != arc+1:
                    enemy[t][2] += 1
                    end += 1
        forward += 1    # 탐색이 다 끝났으면 한 칸 전진
    if sub > ans:       # while문이 다 끝났을 때 sub가 ans보다 크다면 갱신!
        ans = sub
print(ans)