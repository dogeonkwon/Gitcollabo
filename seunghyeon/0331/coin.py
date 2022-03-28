# coin[]: 동전의 금액을 저장, choice[]: 선택한 동전들 집합
# best: 거스름돈에 대한 최소 동전 개수


def CoinChange(choice, N, money):
    global best

    if best <= N:     # 현재까지 발견된 최적의 해보다 현재 선택된 동전의 개수가 더 크면 해가 아님.
        return
    elif money == 0:  # 거스름돈 = 0: 하나의 후보해를 찾았다 !
        best = N      # 거스름돈 0원이 되는 가장 높이가 낮은 단말 노드가 최적해
    else:
        # 거스름돈이 0원이 아니면 선택을 계속함
        for i in range(len(coin)):
            if money - coin[i] >= 0:                      # 선택한 동전이 거스름돈 금액보다 작거나 같으면
                CoinChange(choice + [coin[i]], N+1, money-coin[i])    
                # 선택한 동전 저장
                # 거스름돈 금액을 선택한 동전의 금액만큼 차감


coin = [10, 50, 100, 400, 500]
best = 999999999
CoinChange([], 0, 800)
print(best)