import sys
sys.stdin = open('input.txt','r')

dwarfs = [int(input()) for _ in range(9)]
dwarfs.sort()

# for i in range(1<<9):
#     subset = []
#     for j in range(9):
#         if i&(1<<j):
#             subset.append(dwarf[j])
#     if len(subset) == 7 and sum(subset) == 100:
#         for i in range(7):
#             print(subset[i])

for i in range(8):
    for j in range(i+1, 9):
        if sum(dwarfs) - dwarfs[i] - dwarfs[j] == 100:
            dwarf_1, dwarf_2 = dwarfs[i], dwarfs[j]
            dwarfs.remove(dwarf_1)
            dwarfs.remove(dwarf_2)
            for dwarf in dwarfs:
                print(dwarf)
            break
    if len(dwarfs) == 7:
        break

