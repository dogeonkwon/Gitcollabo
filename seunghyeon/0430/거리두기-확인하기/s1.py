# 2022-04-28

def solution(places):
    answer = [0] * 5

    for k in range(5):
        # 사용자가 있는 위치 담기
        spot = []
        for i in range(5):
            for j in range(5):
                if places[k][i][j] == 'P':
                    spot.append((i, j))
        
        # 해당 대기실의 결과저장
        answer[k] = check(spot, k, places)
        
    return answer


def check(spot, k, places):
    for n in range(len(spot)):
        for m in range(n+1, len(spot)):
            # 사람이 있는 거리 비교
            d = abs(spot[n][0]-spot[m][0]) + abs(spot[n][1]-spot[m][1])
            
            # 거리가 1이면 => 0
            if d == 1:
                return 0
            
            # 거리가 2일 때
            elif d == 2:
                # 만일 행이나 열이 같으면
                if spot[n][0] == spot[m][0] or spot[n][1] == spot[m][1]:
                    r = (spot[n][0]+spot[m][0]) // 2
                    c = (spot[n][1]+spot[m][1]) // 2

                    # 사이에 파티션이 없으면 => 0
                    if places[k][r][c] != 'X':
                        return 0
                
                # 대각선 상에 있을 때
                else:
                    r1, c1 = spot[n][0], spot[m][1]
                    r2, c2 = spot[m][0], spot[n][1]
                    
                    # 두 사람 사이에 파티션이 없으면 => 0
                    if places[k][r1][c1] != 'X' or places[k][r2][c2] != 'X':
                        return 0
                
    return 1