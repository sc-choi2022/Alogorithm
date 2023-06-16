import sys

# 테스트케이스 수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 날의 수 N
    N = int(sys.stdin.readline())
    # 주가를 담은 배열 stocks
    stocks = list(map(int, sys.stdin.readline().split()))
    # 판매를 통해 얻은 수익 result
    result = 0
    # 가장 마지막 주식의 가격
    number = stocks[-1]
    # 구매한 주식의 개수 cnt, 지불한 비용 paid
    cnt, paid = 0, 0
    # 마지막 날부터 for문을 시작
    for i in range(N-2, -1, -1):
        # 판매가능한 최대 가격이 변경되지 않는 경우
        if stocks[i] <= number:
            cnt += 1
            paid += stocks[i]
        # 판매가능한 최대 가격의 갱신이 필요한 경우
        else:
            result += cnt*number
            number = stocks[i]
            cnt = 0
    # 최대 이익을 출력
    print(result+cnt*number-paid)