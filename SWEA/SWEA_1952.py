import sys
sys.stdin = open('sample_input.txt')
def dfs(n, cost):
    global ans
    # 12월까지 비용이 지불되었다면 ans와 cost를 비교하여 적은 값을 cost에 저장
    if n > 12:
        if ans > cost:
            ans = cost
        return
    # 일일권
    dfs(n+1, cost + lst[n]*day)
    # 월간권
    dfs(n+1, cost + mon)
    # 분기권
    dfs(n+3, cost + mon3)
    # 연간권
    dfs(n+12, cost + year)

T = int(input())
for case in range(1, T+1):
    # 일일권, 월간권, 분기권, 연간권의 가격을 day, mon, mon3, year에 반영
    day, mon, mon3, year = map(int, input().split())
    # idx월에 값을 넣어주기 위해 [0]를 앞에 추가
    lst = [0] + list(map(int, input().split()))

    ans = 36000
    # 1월을 선택해야함을 표시 가격 0원
    dfs(1, 0)
    # 테스트케이스와 최소 지출 비용을 출력
    print(f'#{case} {ans}')