# BOJ_2477_참외밭
# 2022-03-05

cnt = int(input())  # 1m^2에 있는 참외수
length = [tuple(map(int, input().split())) for _ in range(6)]  # 반시계방향 / 1: 동, 2: 서, 3: 남, 4:북 / 길이
counts = [0] * 5    # 방향이 나온 개수
area = 0            # 결과 면적

# 방향이 몇 번 나왔는가? >> 1번 나온 방향이 가로 or 세로최대길이
for t in length:
    counts[t[0]] += 1

# 가로, 세로가 가장 긴 변은 무조건 이어져서 나옴
# 방향이 정해져 있으므로(반시계), 전체 면적 - 잘린 면적 = 참외밭의 면적
if counts[1] == 1:
    if counts[4] == 1:
        for n in range(6):
            if length[n][0] == 1:
                idx_1 = n
            if length[n][0] == 4:
                idx_4 = n
        area = length[idx_1][1] * length[idx_4][1]
        if idx_4 == 5:
            area -= length[1][1] * length[2][1]
        elif idx_4 == 4:
            area -= length[0][1] * length[1][1]
        elif idx_4 == 3:
            area -= length[5][1] * length[0][1]
        else:
            area -= length[idx_4+2][1] * length[idx_4+3][1]

    elif counts[3] == 1:
        for n in range(6):
            if length[n][0] == 1:
                idx_1 = n
            if length[n][0] == 3:
                idx_3 = n

        area = length[idx_1][1] * length[idx_3][1]
        if idx_1 == 5:
            area -= length[1][1] * length[2][1]
        elif idx_1 == 4:
            area -= length[0][1] * length[1][1]
        elif idx_1 == 3:
            area -= length[5][1] * length[0][1]
        else:
            area -= length[idx_1+2][1] * length[idx_1+3][1]


elif counts[2] == 1:
    if counts[4] == 1:
        for n in range(6):
            if length[n][0] == 2:
                idx_2 = n
            if length[n][0] == 4:
                idx_4 = n

        area = length[idx_2][1] * length[idx_4][1]
        if idx_2 == 5:
            area -= length[1][1] * length[2][1]
        elif idx_2 == 4:
            area -= length[0][1] * length[1][1]
        elif idx_2 == 3:
            area -= length[5][1] * length[0][1]
        else:
            area -= length[idx_2+2][1] * length[idx_2+3][1]

    elif counts[3] == 1:
        for n in range(6):
            if length[n][0] == 2:
                idx_2 = n
            if length[n][0] == 3:
                idx_3 = n

        area = length[idx_2][1] * length[idx_3][1]
        if idx_3 == 5:
            area -= length[1][1] * length[2][1]
        elif idx_3 == 4:
            area -= length[0][1] * length[1][1]
        elif idx_3 == 3:
            area -= length[5][1] * length[0][1]
        else:
            area -= length[idx_3+2][1] * length[idx_3+3][1]

print(area*cnt)