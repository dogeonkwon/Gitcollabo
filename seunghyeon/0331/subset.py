def subset(a, k, n):
    if k == n:                     # 모든 선택이 끝난 상태
        return print(a)
    else:                          # k가 n에 도달하지 않았다면,
        a[k] = 0                   # k번째 원소를 포함하지 않는다는 의미
        subset(a, k+1, n)          # k를 증가시킨 값을 매개변수로 재귀 호출
        a[k] = 1                   # k번째 원소를 포함한다는 의미
        subset(a, k+1, n)          # k를 증가시킨 값을 매개변수로 재귀 호출



subset([0, 0, 0], 0, 3)