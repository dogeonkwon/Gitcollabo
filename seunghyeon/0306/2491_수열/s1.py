# 2491_수열 풀이
# 2022-02-27

N = int(input())   # 숫자의 개수
nums = list(map(int, input().split()))   # 숫자 받아오기
cnt_1 = 1       # 크거나 같을 때, 카운팅
cnt_2 = 1       # 작거나 같을 때, 카운팅
max_cnt = 0     # 최고 카운팅 값

# 도건빵이 찾은 에러
if N == 1:
    max_cnt = 1

for n in range(N-1):
    # 다음 수가 나보다 크거나 같을 때, 카운팅
    if nums[n] <= nums[n+1]:
        cnt_1 += 1
        if max_cnt < cnt_1:
            max_cnt = cnt_1
    # 아니면 초기화
    else:
        cnt_1 = 1

    # 다음 수가 나보다 작거나 같을 때, 카운팅
    if nums[n] >= nums[n+1]:
        cnt_2 += 1
        if max_cnt < cnt_2:
            max_cnt = cnt_2
    # 아니면 초기화
    else:
        cnt_2 = 1

print(max_cnt)

