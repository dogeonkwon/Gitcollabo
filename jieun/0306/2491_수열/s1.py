N = int(input())
numbers = list(map(int, input().split()))

# 정방향 수열로 알아보기
ans = 1
cnt =1
# 인덱스는 1부터 마지막까지
for i in range(1, N):
    # 전 숫자가 자기 자신보다 작거나 같다면 count 추가
    if numbers[i-1] <= numbers[i]:
        cnt+=1
    # 아니라면 count 그냥 1
    else:
        cnt = 1
    # 위의 if 절 한번 돌때마다 cnt와 ans 비교해서 큰 숫자 넣기
    if ans< cnt:
        ans = cnt

# 역방향 수열로 알아보기
number_r = numbers[::-1]
ans_r = 1
cnt_r = 1
for i in range(1, N):
    if number_r[i-1] <= number_r[i]:
        cnt_r +=1
    else:
        cnt_r = 1

    if ans_r < cnt_r:
        ans_r = cnt_r

# 순방향, 역방향 다 알아보고 가장 큰 크기 넣기
print(max(ans, ans_r))
