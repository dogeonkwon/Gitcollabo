def solution(id_list, report, k):
    N = len(id_list)    # 사용자 수
    answer = [0] * N  
    arr = [[0] * N for _ in range(N)]
    lst = [0] * N
    
    for rep in report:
        a, b = rep.split()
        a_idx = id_list.index(a)
        b_idx = id_list.index(b)
        
        # 사용자a가 b를 이미 신고했다면 재신고 불가
        if arr[a_idx][b_idx]:
            continue
            
        # a가 b를 신고한적 없을 때, 신고
        arr[a_idx][b_idx] = 1
        lst[b_idx] += 1
    
    # 결과 구하기
    for n in range(N):
        for m in range(N):
            # n번 사용자가 m번을 신고한 경우
            # m번 사용자가 정지당했는지 확인
            if arr[n][m] and lst[m] >= k:
                answer[n] += 1
    
    return answer