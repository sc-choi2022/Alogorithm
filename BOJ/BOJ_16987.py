import sys

def hit(idx, cnt):
    global answer

    if idx == N or cnt == N-1:
        answer = max(answer, cnt)
        return
    # idx번째 계란이 이미 깨진 경우
    if S[idx] <= 0:
        hit(idx+1, cnt)
    else:
        for e in range(N):
            if e == idx:
                continue
            # e번째 계란이 깨지지 않은 계란인 경우
            if S[e] > 0:
                S[e], S[idx] = S[e]-W[idx], S[idx]-W[e]
                if S[e] <= 0 and S[idx] <= 0:
                    hit(idx+1, cnt+2)
                elif S[e] <= 0 or S[idx] <= 0:
                    hit(idx+1, cnt+1)
                else:
                    hit(idx+1, cnt)
                S[e], S[idx] = S[e]+W[idx], S[idx]+W[e]

# 계란의 수 N
N = int(sys.stdin.readline())
# 계란의 내구성을 저장하는 배열 S, 계란의 무게를 저장하는 배열 W
S, W = [0] * N, [0] * N

for i in range(N):
    S[i], W[i] = map(int, sys.stdin.readline().split())

# 깰 수 있는 계란의 최대 개수 answer
answer = 0
hit(0, 0)

# answer을 출력
print(answer)