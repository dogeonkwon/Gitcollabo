# P의 좌표를 찾자.
def findP(room):
    tmp = []
    for i in range(5):
        for j in range(5):
            if room[i][j] == 'P':
                tmp.append([i, j])

    return tmp


# P와 붙어 있는 O의 좌표를 찾자.
def findO(p, room):
    tmp = []

    for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):  # 상우하좌
        nr = p[0] + dr
        nc = p[1] + dc

        if 0 <= nr < 5 and 0 <= nc < 5:

            # 놓친 테스트 케이스
            # P 바로 옆에 P가 있다면 거리두기 못지킨것, break 하고 함수 빠져나가자
            if room[nr][nc] == 'P':
                tmp = 'break'
                break

            elif room[nr][nc] == 'O':
                tmp.append([nr, nc])

    return tmp


def solution(places):
    answer = []

    for place in places:

        # P의 좌표를 받아오자
        ppos = findP(place)

        # P가 하나도 없다면 거리두기 지킨 것
        if len(ppos) == 0:
            answer.append(1)
            pass

        # P가 존재 한다면 거리두기 확인 하기
        else:
            for p in ppos:
                ans = 1

                # P와 연결된 O의 좌표를 리스트로 받는다.
                opos = findO(p, place)

                # 만약 P 바로 옆에 P가 있다면 ans = 0으로 만들고 answer에 추가 한다.
                if opos == 'break':
                    ans = 0
                    break

                # O에서 다시 델타 탐색을 통해 P를 찾는다.
                for o in opos:
                    for dr, dc in ((-1, 0), (0, 1), (1, 0), (-1, 0)):  # 상우하좌
                        nr = o[0] + dr
                        nc = o[1] + dc
                        if 0 <= nr < 5 and 0 <= nc < 5:

                            # 자신은 거리두기 대상이 되지 않는다.
                            if nr == p[0] and nc == p[1]:
                                break

                            # O 옆에 P가 있다면 거리두기 실패한 케이스 이다.
                            elif place[nr][nc] == 'P':
                                ans = 0
                                break

                    if ans == 0:
                        break
                if ans == 0:
                    break

            answer.append(ans)

    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))