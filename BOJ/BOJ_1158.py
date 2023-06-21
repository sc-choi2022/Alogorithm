from collections import deque
import sys

# 사람의 수 N, 양의 정수 K
N, K = map(int, sys.stdin.readline().split())
# popleft를 활용하기 위해 deque를 사용하여 queue 생성
queue = deque(range(1,N+1))
print('<', end='')
# N개의 수만큼
for i in range(N-1):
    # K번째 수를 찾고
    for j in range(K-1):
        queue.append(queue.popleft())
    # 제거된 수를 출력
    print(str(queue.popleft())+',', end=' ')
print(str(queue.popleft())+'>')

# 사람의 수 N, 양의 정수 K
N, K = map(int, sys.stdin.readline().split())

queue = list(range(1, N+1))
result = []
idx = 0
while queue:
    # K번째 사람을 제거하고 result에 추가
    idx = (idx + (K - 1)) % len(queue)
    result.append(queue.pop(idx))
# 조건에 맞게 출력
print('<' + ', '.join(map(str, result)) + '>')

# 요세푸스 문제 풀이 2
import sys

# 사람의 명수 N, 양의 정수 K
N, K = map(int, sys.stdin.readline().split())
# 제거를 위치를 저장하는 변수 idx
idx = 0
# 사람의 수를 담은 배열 numbers
numbers = [x for x in range(1, N+1)]

# 요세푸스 순열을 출력
print('<', end='')
for i in range(N-1):
    idx = (idx+K-1)%len(numbers)
    print(numbers.pop(idx), end=', ')
print(numbers.pop(), end='>')