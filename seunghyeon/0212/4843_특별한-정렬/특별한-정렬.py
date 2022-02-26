# 특별한-정렬
# 2022-02-12

import sys

sys.stdin = open('sample_input.txt', 'r')
T = int(input())

for tc in range(1, T+1):
    # N: 정수의 개수
    # nums: 숫자들의 리스트
    N = int(input())
    nums = list(map(int, input().split()))

    # 가장큰수, 가장작은수를 구해서 앞으로 뺀 후,
    # 두 수를 제외한 뒷 인덱스부터 보면 된다 !
    for n in range(0, 10, 2):

        # 가장 큰수와 가장 작은 수 정렬
        for m in range(n, N):

            # 가장 큰수를 앞으로 빼줘
            if nums[n] <= nums[m]:
                nums[n], nums[m] = nums[m], nums[n]

            # 가장 작은 수를 앞으로 빼줘
            if nums[n+1] >= nums[m]:
                nums[n+1], nums[m] = nums[m], nums[n+1]

    print('#{}'.format(tc), end='')

    for num in range(10):
        if num == 9:
            print(' {}'.format(nums[num]))
        else:
            print(' {}'.format(nums[num]), end='')
