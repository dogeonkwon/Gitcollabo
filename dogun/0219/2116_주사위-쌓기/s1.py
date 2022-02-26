# 2116_주사위-쌓기
# 2022-02-19

import sys
sys.stdin = open('input.txt', 'r')

def maxi(lst):      # 최대값을 찾아주는 함수

    ret = 0
    for i in lst:
        if ret < i:
            ret = i
    return ret


N = int(input())        # 주사위의 개수

dice = [list(map(int, input().split())) for _ in range(N)]      # 각 면에 적혀지는 주사위 숫자

result = 0      # 최종 결과값

for i in dice[0]:       # 주사위가 제일 아래에서 출발하므로
    A = dice[0][0]      # A~F까지 숫자를 다 입력
    B = dice[0][1]
    C = dice[0][2]
    D = dice[0][3]
    E = dice[0][4]
    F = dice[0][5]

    dic = {A:F, B:D, C:E, D:B, E:C, F:A}        # 각 면과 마주하는 면을 딕셔너리로 엮어줌

    max_num = 0         # 최대값
    v = dic[i]          # 첫 주사위의 바닥에 깔린 면에 대응하는 면
    sub_lst = [k for k in dice[0] if k not in [v, i]]       # 바닥면과 대응하는 면을 뺀 나머지 수들의 리스트
    max_num += maxi(sub_lst)        # 거기서 최대값을 구해서 max_num에 더해줌

    for j in range(1, N):       # 제일 아래면이 정해졌으면 N개까지 A~F를 재설정해주고 위와 마찬가지로 계산
        A = dice[j][0]
        B = dice[j][1]
        C = dice[j][2]
        D = dice[j][3]
        E = dice[j][4]
        F = dice[j][5]

        dic = {A: F, B: D, C: E, D: B, E: C, F: A}

        w = dic[v]
        sub_lst2 = [n for n in dice[j] if n not in [w, v]]
        max_num += maxi(sub_lst2)
        v = w

    if result < max_num:        # 만약 최대값이 결과값보다 크다면 결과값을 바꿔줌
        result = max_num
    else:
        continue

print(result)