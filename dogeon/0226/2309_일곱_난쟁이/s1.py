# 2309_일곱-난쟁이 풀이
# 2022-02-26


# 합계를 구하는 함수
def my_sum(s):
    tal = 0
    for v in s:
        tal += v
    return tal


N = 9                                  # 원소의 개수만큼

arr = list()
for _ in range(9):
    arr += map(int, input().split())        # arr에 +를 해주면서 입력값을 받아온다

lst = list()            # 뺄 숫자를 담아줄 리스트
result = list()         # 결과값을 담아줄 리스트

for i in range(9):          # 9개의 값이 있으므로 1번씩 다 넣어준다.
    total = my_sum(arr)
    total -= arr[i]
    j = 0
    while j < 9:            # 그리고 같은 값은 제외하고 빼서 100이 되는 값을 찾아준다.
        if j == i:
            j += 1
            continue
        elif total - arr[j] == 100:
            lst = [arr[i], arr[j]]
            result = [k for k in arr if k not in lst]       # 찾은 값과 겹치지 않는 값들을 result에 모아준다.
            break
        else:
            j += 1


for n in range(6):                  # result를 정렬
    for m in range(n+1, 7):
        if result[n] > result[m]:
            result[n], result[m] = result[m], result[n]

for l in result:
    print(l)