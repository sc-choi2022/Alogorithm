import sys
# 달갈의 개수 N, 잠재적 고객 M명
N, M = map(int, sys.stdin.readline().split())
# 고객이 구매를 결정하는 달걀의 가격 P
P = sorted([int(sys.stdin.readline()) for _ in range(M)])
# 책정한 가격 price, price로 올릴 수 있는 수익 profit
price, profit = 0, 0

for i in range(M):
    # P[i]을 기준으로 구한 예상 수익 tmp
    # 최대 1개의 달걀을 판매하므로 최대 N명 인덱스에 따른 M - i개 판매 가능
    tmp = P[i] * (M - i if M - i <= N else N)

    # tmp가 기존 예상 수익보다 높은 경우 profit, price을 재설정
    if profit < tmp:
        profit = tmp
        price = P[i]
# 책정한 가격과 이 가격으로 올릴 수 있는 수익을 출력
print(price, profit)