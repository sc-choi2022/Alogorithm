from collections import defaultdict
import sys

# 주어지는 문자열 S
S = sys.stdin.readline().rstrip()
# 소들의 첫 점을 지난 여부를 저장하는 딕셔너리 cows
cows = defaultdict(int)
# 소들의 등장 순서대로 저장하는 배열 stack
stack = []
# 경로가 무조건 만나는 소의 수 answer
answer = 0

for s in S:
    cows[s] += 1
    # 소가 들어오는 경우 stack에 추가
    if cows[s] == 1:
        stack.append(s)
    else:
        # 현재 소가 다른 소와 경로가 겹치지 않는 경우
        if stack[-1] == s:
            stack.pop()
        # 현재 소가 다르 소와 경로가 겹치는 경우
        else:
            # 현재 소의 들어온 위치 N, stack의 길이 L
            N = stack.index(s)
            L = len(stack)
            # 경로가 겹치는 소의 쌍을 answer에 추가
            answer += L - N - 1
            # 현재 소를 stack에서 제거
            stack.pop(N)
# 경로가 무조건 만나는 소가 몇 쌍인지 출력
print(answer)