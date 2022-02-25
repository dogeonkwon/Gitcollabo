#데이터가져오기
import sys
sys.stdin = open('input.txt','r')
#난쟁이 리스트 가져오기
dwarfs = [int(input()) for _ in range(9)]
dwarfs.sort()
#부분집합 구하기
# for i in range(1<<9):
#     subset = []
#     for j in range(9):
#         if i&(1<<j):
#             subset.append(dwarf[j])
#     if len(subset) == 7 and sum(subset) == 100:
#         for i in range(7):
#             print(subset[i])

# 난쟁이중에서 2명 추출
for i in range(8):
    for j in range(i+1, 9):
        # 난쟁이 전체 합 중에서 난쟁이1, 난쟁이2 의 키 빼서 100이면
        if sum(dwarfs) - dwarfs[i] - dwarfs[j] == 100:
            dwarf_1, dwarf_2 = dwarfs[i], dwarfs[j]
            # 난쟁이에서 제거
            dwarfs.remove(dwarf_1)
            dwarfs.remove(dwarf_2)
            for dwarf in dwarfs:
                print(dwarf)
            break
    # 이미 한번 돈 i에서 빠졌다면 멈쳐줘, 안그러면 이미 i와 j가빠진 상태에서 계속 돌아가면 인덱스 에러가 난다!
    if len(dwarfs) == 7:
        break

