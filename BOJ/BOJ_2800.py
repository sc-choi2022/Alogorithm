import sys

def dfs(idx, result, cnt):
    if idx == L:
        # 올바른 괄호 쌍을 만든 경우
        if cnt == 0 and result != equation:
            answer.add(result)
        return

    if equation[idx] == '(':
        visit[idx] = 1
        dfs(idx+1, result+equation[idx], cnt+1)
        visit[idx] = 0
        dfs(idx+1, result, cnt)
    elif equation[idx] == ')':
        if visit[pair[idx]] and cnt > 0:
            dfs(idx+1, result+equation[idx], cnt-1)
        else:
            dfs(idx+1, result, cnt)
    else:
        dfs(idx+1, result+equation[idx], cnt)

# 음이 아닌 정수로 이루어진 수식 equation
equation = sys.stdin.readline().rstrip()
L = len(equation)
# 올바른 괄호 쌍을 저장하는 셋 answer
answer = set()
# 괄호쌍의 사용 여부를 저장하는 배열 visit
visit = [0] * L
# 괄호쌍의 위치를 저장하는 딕셔너리 pair
pair = {}
stack = []

for i in range(L):
    if equation[i] == '(':
        stack.append(i)
    elif equation[i] == ')':
        pair[i] = stack.pop()

dfs(0, '', 0)

# 올바른 괄호 쌍을 제거해서 나올 수 있는 서로 다른 식을 사전 순으로 출력
for a in sorted(list(answer)):
    print(a)