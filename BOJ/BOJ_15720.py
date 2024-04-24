import sys

# 주문한 버거의 개수 B, 사이드 메뉴의 개수 C, 음료의 개수 D
B, C, D = map(int, sys.stdin.readline().split())
# 버거의 가격 burgers
burgers = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
# 사이드 메뉴의 가격 side
side = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
# 음료의 개수 drinks
drinks = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
answer = sum(burgers)+sum(side)+sum(drinks)
# 세트 할인이 적용되기 전 가격을 출력
print(answer)

for i in range(min(B, C, D)):
    answer -= (burgers[i]+side[i]+drinks[i])*0.1
# 세트 할인이 적용된 후의 최소 가격을 출력
print(int(answer))