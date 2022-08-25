# 영수증에 제시된 금액 X
X = int(input())

# 영수증에 적힌 구매한 물건의 종류의 수 N
N = int(input())

ans = 0
for _ in range(N):
    # 물건의 가격 a, 개수 b
    a, b = map(int, input().split())
    ans += a * b
# 구매한 물건의 가격과 개수로 계산한 금액에 영수증 총 금액과 일치하면 Yes 출력
if X == ans:
    print('Yes')
# 일치하지 않는다면 No 출력
else:
    print('No')