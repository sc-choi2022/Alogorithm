import sys
# 테스트 케이스 수
T = int(sys.stdin.readline())

for _ in range(T):
    # 최소공배수를 구해야하는 수 A, B
    A, B = map(int, sys.stdin.readline().split())

    if A == B:
        print(A)
        break
    else:
        cnt = 1
        less = min(A, B)
        more = max(A, B)
        ans = 1
        while less >= cnt:
            if less % cnt or more % cnt:
                cnt += 1
                continue
            cnt += 1
            ans = cnt
        print(ans)
        print(ans * (A//ans) * (B//ans))