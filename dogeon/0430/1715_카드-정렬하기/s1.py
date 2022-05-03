# 1715_카드-정렬하기 풀이
# 2022-04-30

import heapq

n = int(input())
cards = [int(input()) for _ in range(n)]
heapq.heapify(cards)   # 리스트 cards를 선형 시간으로 제자리에서 힙으로 변환
ans = 0

while len(cards) > 1:
    a = heapq.heappop(cards)   # 힙 불변성을 유지하면서, cards에서 가장 작은 항목을 팝하고 반환. 힙이 비어 있으면, IndexError가 발생. 팝 하지 않고 가장 작은 항목에 액세스하려면, heap[0]을 사용
    b = heapq.heappop(cards)
    heapq.heappush(cards, (a+b))    # 힙 불변성을 유지하면서, (a+b)값을 cards으로 푸시
    ans += (a+b)
print(ans)


# 시간초과가 계속 남
'''
N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort(reverse=True)
res = 0
lst = list()

if N == 1:
    res = arr[0]
elif N == 2:
    res = sum(arr)
else:
    sub = arr.pop() + arr.pop()
    res += sub
    lst.append(sub)
    while len(arr) > 1:
        a = arr.pop()
        res += a
        b = 0
        lst.sort(reverse=True)
        if arr[-1] > lst[-1]:
            b = lst.pop()
            res += b
        else:
            b = arr.pop()
            res += b
        lst.append((a+b))
    for n in arr:
        res += n
    for m in lst:
        res += m
print(res)
'''
# 4
# 30
# 40
# 50
# 60