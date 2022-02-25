import sys
sys.stdin = open('input.txt')

# 테스트케이스 개수
T = int(input())
# S마켓에서 사용하는 돈의 종류를 내림차순으로 담은 리스트 money
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
# 거스름돈의 종류별 개수를 담을 리스트 ans
ans = [0]*8

for case in range(1, T+1):
    # 거슬러 주어야하는 금액 N
    N = int(input())
    # 사용하는 돈의 모든 종류에 대해
    for i in range(len(money)):
        # 거스름 돈의 수
        change = N//money[i]
        # ans에 추가
        ans[i] = change
        # ans에 추가된 돈만큼 제외
        N -= change*money[i]
    # 테스트케이스 번호 출력
    print(f'#{case}')
    # 각 돈의 종류마다 필요한 개수를 빈칸을 사이에 두고 출력
    print(*ans)