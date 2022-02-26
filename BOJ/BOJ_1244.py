# 스위치의 개수
N = int(input())
# 스위치의 상태
status = list(map(int, input().split()))

S = int(input())
for _ in range(S):
    # 성별 G, 받은 번호 Numb
    G, numb = map(int, input().split())
    # 남자일 경우
    if G == 1:
        # numb의 배수에서 스위치 상태 변경
        for x in range(numb-1, N, numb):
            if status[x] == 1:
                status[x] = 0
            elif status[x] == 0:
                status[x] = 1
    # 여자일 경우
    elif G == 2:
        # numb값을 기준으로 최대 좌우 길이 N-1//2를 기준으로
        for y in range(N-1//2):
            # 좌우로 y만큼 움직였을 때 범위 안에 있고, 두 값이 동일하다면
            if 0 <= numb-1-y <N and 0<= numb-1+y <N and status[numb-1-y] == status[numb-1+y]:
                # 스위치 상태를 변경
                if status[numb-1-y] == 1:
                    status[numb-1-y] = 0
                    status[numb-1+y] = 0
                elif status[numb-1-y] == 0:
                    status[numb-1-y] = 1
                    status[numb-1+y] = 1
            else:
                break
# 1번부터 마지막 스위치의 상태를 한 줄에 20개씩 출력
for s in range(0, len(status), 20):
    print(*status[s:s+20])