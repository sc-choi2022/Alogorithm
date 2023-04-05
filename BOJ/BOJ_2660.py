from collections import defaultdict, deque
import sys

def countNumber(memberI):
    queue = deque([(memberI, 0)])

    while queue:
        num, cnt = queue.popleft()

        for m in member[num]:
            if not visit[m]:
                queue.append((m, cnt + 1))
                visit[m] = 1
                score[memberI] = max(score[memberI], cnt + 1)

# 회원의 수 N
N = int(sys.stdin.readline())
# 회원의 친구를 배열로 저장할 딕셔너리 member
member = defaultdict(list)
# 회원의 친구점수를 저장할 배열 score
score = [N] + [0] * N

while True:
    # 친구관계인 회원 a, b
    a, b = map(int, sys.stdin.readline().split())

    if a == -1 and b == -1:
        break

    member[a].append(b)
    member[b].append(a)

# 각 회원의 친구점수를 확인인
for i in range(1, N+1):
    visit = [1] + [0] * N
    visit[i] = 1
    countNumber(i)

# 회장 후보의 점수 number
number = min(score)
# 회장 후보를 저장하는 배열 candidate
candidate = [j for j in range(1, N+1) if score[j] == number]

# 회장 후보의 점수와 후보의 수를 출력
print(number, len(candidate))
# 회장 후보를 오름차순으로 모두 출력
print(*candidate)