T = int(input())
# 모든 테스트 케이스
for case in range(1, T+1):
    # 신청한 화물차 수 N
    N = int(input())
    # N개의 화물차의 신청한 시작과 종료시간을 담은 리스트 req
    req = [list(map(int, input().split())) for _ in range(N)]
    # 종료시간을 기준으로 req를 정렬
    req.sort(key=lambda x: x[1])

    # 가장 빠른 종료시간을 가진 화물차의 시간을 start와 end 변수에 할당
    start, end = req.pop(0)
    ans = 1
    # 리스트 req가 비어있게 될 때까지
    while req:
        # 다음 화물차 시작시간과 종료시간을 next_start, next_end 변수에 할당
        next_start, next_end = req.pop(0)
        # 다음 화물차의 시작시간이 이전 화물차의 종료시간보다 같거나 크다면
        if next_start >= end:
            # 화물차의 개수 1증가, start와 end값을 재할당
            ans += 1
            start = next_start
            end = next_end
    # 테스트케이스번호와 ans 출력
    print(f'#{case} {ans}')