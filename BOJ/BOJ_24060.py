import sys

def mergeSort(L):
    if len(L) == 1:
        return L

    mid = (len(L) + 1) // 2
    left = mergeSort(L[:mid])
    right = mergeSort(L[mid:])

    L2 = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            L2.append(left[i])
            ans.append(left[i])
            i += 1
        else:
            L2.append(right[j])
            ans.append(right[j])
            j += 1

    while i < len(left):
        L2.append(left[i])
        ans.append(left[i])
        i += 1

    while j < len(right):
        L2.append(right[j])
        ans.append(right[j])
        j += 1

    return L2

# 배열 A의 크기 N, 저장 횟수 K
N, K = map(int, sys.stdin.readline().split())
# 배열 A
A = list(map(int, sys.stdin.readline().split()))
# 저장되는 수 ans
ans = []
mergeSort(A)

# 배열 A에 K번째 저장 되는 수를 출력
if len(ans) >= K:
    print(ans[K - 1])
# 저장 횟수가 K보다 작으면 -1 출력
else:
    print(-1)