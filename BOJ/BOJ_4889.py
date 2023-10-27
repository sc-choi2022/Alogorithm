import sys

answer = []

while True:
    stack = []
    cnt = 0
    S = sys.stdin.readline().rstrip()

    if '-' in S:
        break
    for i in range(len(S)):
        if not stack and S[i] == '}':
            cnt += 1
            stack.append('{')
        elif stack and S[i] == '}':
            stack.pop()
        else:
            stack.append(S[i])
    cnt += len(stack)//2
    answer.append(cnt)

for j in range(1, len(answer)+1):
    print(j+1, '. ', answer[j-1], sep='')