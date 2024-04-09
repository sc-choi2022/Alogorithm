from collections import defaultdict
import sys

# 참가자의 수 N
N = int(sys.stdin.readline())
# 참가자의 이름을 저장하는 딕셔너리 participate
participate = defaultdict(int)

for _ in range(N):
    participate[sys.stdin.readline().rstrip()] += 1

for _ in range(N-1):
    name = sys.stdin.readline().rstrip()
    participate[name] -= 1
    # 참가자가 모두 완주한 겨우 제외
    if participate[name] == 0:
        del participate[name]

# 마라톤을 완주하지 못한 참가자의 이름을 출력
print(list(participate.keys())[0])