# order[]: 순열의 순서를 저장하는 리스트(원소들에 대한 인덱스 값들이 저장되어 있음)

def permutation(order, k, n):
    if k == n:               # 단말노드에 도달한 경우
        print(*order)
        return
    
    check = [False]*n        # 현재 방문중인 노드에 도달하기까지 어떤 선택을 했는지 조사하기 위해 사용
    
    # k개만큼 선택한 내용이 저장되어 있음
    for i in range(k):
        check[order[i]] = True
    
    # 원소들의 수만큼 check 리스트를 조사
    for i in range(n):
        if check[i] == False:            # i가 선택되지 않으면,
            order[k] = i                 # i를 선택
            permutation(order, k+1, n)   # 다음 선택을 위해 재귀 호출

permutation([0, 0, 0, 0], 0, 4)