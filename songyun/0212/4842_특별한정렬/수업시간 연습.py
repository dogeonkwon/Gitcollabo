import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input()) # N = 정수의 갯수

    arr = list(map(int, input().split()))

    for k in range(0, N, 2):

        for i in range(k, N):
            if arr[i] >= arr[k]:
               arr[i],arr[k] = arr[k], arr[i]

            elif arr[k+1] >= arr[i]:
                arr[k+1], arr[i] = arr[i], arr[k+1]
    print(arr)

