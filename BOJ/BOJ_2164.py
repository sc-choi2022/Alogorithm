from collections import deque

# 카드의 수 N
N = int(input())
# queue 활용하기 위해 deque 사용
last = deque()
# 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드를 놓는다.
for i in range(1, N + 1):
    last.append(i)

# 반복되는 동작을 카드가 하나가 될때 까지 진행한다.
while len(last) > 1:
    # 제일 위의 카드를 버린다.
    last.popleft()
    # 카드의 수를 확인한다.
    if len(last) == 1:
        break
    # 제일 위의 카드를 가장 아래로 움직인다.
    last.append(last.popleft())

# 제일 마지막에 남는 카드를 출력한다.
print(last.popleft())