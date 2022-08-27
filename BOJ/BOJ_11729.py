# 배열 A의 크기 N
N = int(input())
# 배열 A
A = list(map(int, input().split()))
# 출력할 배열 P값을 -1로 초기화
P = [-1]*N
# P에 값으로 넣어줄 idx을 0 초기화
idx = 0
for _ in range(N):
    # A에서 가장 작은 값의 index을 min_idx에 저장
    min_idx = A.index(min(A))
    # A[min_idx] 값을 범위 밖인 1001로 저장
    A[min_idx] = 1001
    # P[min_idx]에 값 idx 저장
    P[min_idx] = idx
    idx += 1
# P 출력
print(*P)