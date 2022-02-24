import sys
sys.stdin = open('input.txt')
T = int(input())
for case in range(1, T+1):
    # 손님의 수 N, M초의 시간에 만드는 붕어빵 K
    N, M, K = map(int, input().split())
    # N명의 손님이 오는 시간
    customer = list(map(int, input().split()))
    # customer를 정렬, Bubble Sort
    for i in range(len(customer)-1, 0, -1):
        for j in range(0, i):
            if customer[j] > customer[j + 1]:
                customer[j], customer[j + 1] = customer[j + 1], customer[j]

    # 마지막으로 확인하는 시간
    last = customer[-1]
    ans = 'Possible'
    cnt = 0

    # i 시간대 까지의 빵 개수
    for i in range(N):
        # 정렬 되어 있기 때문에 앞의 수(i-1)만큼 붕어빵이 팔렸을 것
        bread = (customer[i]//M) * K - (i+1)
        if bread < 0:
            ans = "Impossible"
            break
    # 테스트케이스 번호와 붕어빵 제공 여부 제출
    print(f'#{case} {ans}')