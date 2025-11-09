import sys

# 테스트 케이스의 개수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 암호화한 편지 S
    S = sys.stdin.readline().rstrip()
    # 암호화한 편지한 면의 길이 L
    L = int(len(S)**0.5)

    # 원래 메시지를 출력
    for i in range(L-1, -1, -1):
        for j in range(L):
            print(S[i+L*j], end='')
    print()