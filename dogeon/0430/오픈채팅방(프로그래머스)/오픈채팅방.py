# 오픈채팅방(프로그래머스) 풀이
# 2022-04-30


def solution(record):
    answer = []
    nickname = {}

    for i in record[::-1]:      # 최신순으로 닉네임을 설정하기 위해서 뒤에서 부터 탐색한다.
        if i.split()[0] != 'Leave' and i.split()[1] not in nickname:
            nickname[i.split()[1]] = i.split()[2]

    for j in record:        # change는 기록하지 않아도 된다.
        if j.split()[0] == 'Enter':
            answer.append(f"{nickname[j.split()[1]]}님이 들어왔습니다.")
        elif j.split()[0] == 'Leave':
            answer.append(f"{nickname[j.split()[1]]}님이 나갔습니다.")

    return answer