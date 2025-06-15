import sys

# 토핑의 개수 N
N = int(sys.stdin.readline())
# 토핑을 저장하는 배열 topping
toppings = list(set(list(sys.stdin.readline().rstrip().split())))

# 치즈의 개수 cnt
cnt = 0

for topping in toppings:
    if topping[-6:] == 'Cheese':
        cnt += 1

# 주어진 토핑의 목록으로 콰트로치즈피자를 만들 수 있으면 yummy, 만들 수 없으면 sad를 출력
if cnt >= 4:
    print('yummy')
else:
    print('sad')