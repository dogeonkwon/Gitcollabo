# 이진탐색 함수 구현
def binary_search(arr, N, key):
    # arr = 전체 배열
    # N = 배열의 길이
    # key = 찾고자 하는 값

    start = 0 # 시작페이지
    end = N - 1 # 끝 페이지

    while start <= end:
        mid = (start + end) // 2
        if a[mid] == key:
            return True

        elif a[mid] > key:
            end = mid - 1

        else:
            start = mid + 1