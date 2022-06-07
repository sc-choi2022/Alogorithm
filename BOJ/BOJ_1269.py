# 집합 A의 원소의 개수와 집합 B의 원소의 개수 numA, numB
numA, numB = map(int, input().split())

# 집합 A
A = set(map(int, input().split()))
# 집합 B
B = set(map(int, input().split()))

# 차집합의 원소의 개수를 출력
print(len(A^B))