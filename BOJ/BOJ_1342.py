from collections import defaultdict
import sys

def dfs(pre, cnt):
    global answer
    # 행운의 문자열이 완성된 경우
    if cnt == len(S):
        answer += 1
        return
    for key, value in number.items():
        # 행운의 문자열에 부합하지 않는 경우 continue
        if key != pre and value != 0:
            number[key] -= 1
            dfs(key, cnt+1)
            number[key] += 1

# 문자열 S
S = sys.stdin.readline().rstrip()
# 문자열의 각 문자의 개수를 저장하는 딕셔너리 number
number = defaultdict(int)
for s in S:
    number[s] += 1

# 서로 다른 행운의 문자열의 개수
answer = 0
for k in number.keys():
    number[k] -= 1
    dfs(k, 1)
    number[k] += 1

# answer 출력
print(answer)