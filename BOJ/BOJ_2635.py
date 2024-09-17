import sys

# 첫번째 수 N
N = int(sys.stdin.readline())
# 최대 수의 길이 L
L = 0
# 최대 개수의 수를 저장하는 배열 answer
answer = []

for i in range(N, 0, -1):
    tmp = [N, i]
    while True:
        A, B = tmp[-2], tmp[-1]
        # 더 이상 수를 만들지 않는 경우 break
        if A-B < 0:
            break
        tmp.append(A-B)

    if len(tmp) > L:
        L = len(tmp)
        answer = tmp
# 최대 개수를 출력
print(L)
# 첫 번째 수로 시작하여 위의 규칙에 따라 만들 수 있는 수들의 최대 개수를 출력
print(*answer)