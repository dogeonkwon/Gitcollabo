# 2309_일곱난쟁이 풀이
# 2022-02-26

# 난쟁이의 키 리스트
who = [0] * 9
for n in range(9):
    who[n] = int(input())

for i in range(1 << 9):
    cnt = 0                    # 원소의 수 초기화
    part = list()              # 부분집합

    for j in range(9):
        if i & (1 << j):
            cnt += 1             # 원소 수 세기
            part.append(who[j])  # 부분집합 만들기

    if cnt == 7:   # 원소의 수가 7인 부분집합이면 추가
        s = 0
        for p in part:
            s += p

        # 난쟁이의 키의 합이 100이면 찾았당 !
        if s == 100:
            break

# 오름차순 정렬
for n in range(7, -1, -1):
    for m in range(n-1):
        if part[m] > part[m + 1]:
            part[m + 1], part[m] = part[m], part[m + 1]

for p in part:
    print(p)
