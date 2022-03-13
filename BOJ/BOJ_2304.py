# 기둥의 수
N = int(input())
arr = [0]*1001
idx = []
result = 0
for _ in range(N):
    # 왼쪽 면의 위치 L과 높이 H
    L, H = map(int, input().split())
    idx.append(L)
    arr[L] = H
# 위치 값들을 정렬
idx.sort()
# 가장 큰 값의 높이와 위치를 max_h와 max_idx에 담는다.
max_h = max(arr)
max_idx = arr.index(max_h)
# 결과에 가장 큰 값을 더함
result += max_h

# 맨 뒤에서부터 큰 값 전까지
h1 = arr[idx[-1]]
for i in range(idx[-1], max_idx, -1):
    if arr[i] >= h1:
        h1 = arr[i]
    result += h1

# 처음부터 큰 값 전까지
h2 = arr[idx[0]]
for j in range(idx[0], max_idx):
    if arr[j] >= h2:
        h2 = arr[j]
    result += h2
# 다각형의 면적 출력
print(result)