import sys
sys.stdin = open('s_input.txt')

# 테스트케이스 수 T
T = int(input())
# 버스노선 수 N
for case in range(1, T+1):
    # 버스 노선의 개수 N
    N = int(input())
    # 정류장을 지나는 모든 노선을 저장할 stop 딕셔너리
    stop = {}
    # 5000개의 버스 정류장의 노선수를 0으로 초기화
    for i in range(1, 5000+1):
        stop[i] = 0

    # N개의 Aj이상 Bj이하인 모든 정류장을 다니는 노선내용을 stop 딕셔너리에 반영
    for j in range(N):
        S, E = map(int,input().split())
        # 시작과 마지막 정류장의 정보에 포함되는 정류장에 key값을 1 증가
        for i in range(S, E+1):
            stop[i] = stop[i] + 1

    # 출력할 정류장의 개수 P
    P = int(input())
    # 출력할 정류장에 노선 수를 담을 리스트 ans
    ans = []

    # P개의 버스 정류장에 대한 정보를 ans에 담는다
    for p in range(P):
        ans.append(stop[int(input())])

    # 테스트케이스 번호와 ans의 값 출력
    print(f'#{case}', *ans)
