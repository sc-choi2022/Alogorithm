# 테스트 케이스 개수
T = int(input())

for case in range(1, T+1):
    # 노선의 개수
    N = int(input())
    # 정차하는 정보를 담을 리스트
    stop = []
    # 도착 정류장을 통해 확인할 정류장들의 길이를 확인
    len_check = []
    for _ in range(N):
        # 각 노선의 정보를 잠시 담을 리스트 info
        info = list(map(int, input().split()))
        # stop에 info를 추가
        stop.append(info)
        # 도착 정류장 정보를 len_check에 추가
        len_check.append(info[2])

    # len_check를 정렬
    len_check.sort()
    # 가장 큰 값을 M에 할당
    M = max(len_check)
    # M을 기준으로 확인할 리스트의 길이를 결정
    ans = [0] * (M + 1)

    # N개의 노선에 대한 for문
    for i in range(N):
        tmp = stop[i]
        # 버스타입 Bus, 출발 정류장 A, 도착 정류량 B을 받아서 stop에 넣어 준다.
        Bus = tmp[0]
        A = tmp[1]
        B = tmp[2]
        # 일반 노선인 경우
        if Bus == 1:
            for s in range(A, B+1):
                ans[s] += 1
        # 급행 노선인 경우
        elif Bus == 2:
            ans[A] += 1
            ans[B] += 1
            for s in range(A+2, B, 2):
                ans[s] += 1
        # 광역 급행 노선인 경우 중 출발 정류장이 짝수
        elif Bus == 3 and A%2 == 0:
            ans[A] += 1
            ans[B] += 1
            for s in range(A+1, B, 1):
                if s%4 == 0:
                    ans[s] += 1
        # 광역 급행 노선인 경우 중 출발 정류장이 홀수
        elif Bus == 3 and A%2 == 1:
            ans[A] += 1
            ans[B] += 1
            for s in range(A+1, B, 1):
                if s%3 == 0 and s%10 != 0:
                    ans[s] += 1
    # 테스트케이스 번호와 정류장에 최대로 겹치는 노선수 출력
    print(f'#{case} {max(ans)}')