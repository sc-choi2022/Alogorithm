import sys
sys.stdin = open('input.txt')

# 테스트 케이스의 수 T
T = int(input())
for case in range(1,T+1):
    # N개의 일 수
    N = int(input())
    # 각 날의 매매가를 나타내는 N개의 자연수를 담을 리스트 arr
    arr = list(map(int,input().split()))

    # 마지막 날의 값을 임시 가장 큰 값으로 정한다
    max_val = arr[N-1]
    # 최대 이익 profit 값을 초기화
    profit = 0

    # 마지막 날을 바로 전날 부터 첫날까지 for문
    for i in range(N-2, -1, -1):
        # 만약 i날의 값이 기존 max_val보다 크다면 변경
        if arr[i] > max_val:
            max_val = arr[i]
        # 만약 i날의 값이 기존 max_val보다 같거나 작다면 이익을 낼 수 있으므로
        # 최대 이익에 차를 증가
        else:
            profit += max_val - arr[i]
    # 테스트 케이스 번호와 최대 이익
    print(f'#{case} {profit}')