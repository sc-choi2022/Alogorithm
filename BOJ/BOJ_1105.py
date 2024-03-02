import sys

# L보다 크거나 같고 R보다 작거나 같은 기준
L, R = map(str, sys.stdin.readline().split())
answer = 0

if len(L) != len(R):
    print(0)
else:
    N = len(L)
    for i in range(N):
        if L[i] == R[i]:
            if L[i] == '8':
                answer += 1
        else:
            break
    # L보다 크거나 같고, R보다 작거나 같은 자연수 중
    # 8이 가장 적게 들어있는 수에 들어있는 8의 개수를 출력
    print(answer)