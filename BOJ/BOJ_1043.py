import sys

# 사람의 수 N, 파티의수 M
N, M = map(int, sys.stdin.readline().split())
# 진실을 아는 사람의 수 K, 개수만큼의 사람들의 번호 known
known = set(sys.stdin.readline().rstrip().split()[1:])
# 과장된 이야기를 할 수 있는 여부를 저장하는 배열 able
able = [1] * M

for i in range(M):
    # 파티에 오는 사람의 번호를 담은 set numbers
    numbers = set(sys.stdin.readline().rstrip().split()[1:])
    # 파티에 진실을 아는 사람이 있는 경우
    if known.intersection(numbers):
        # 과장된 이야기를 할 수 없으며
        able[i] = 0
        # 진실을 알게된 사람이 추가된다.
        known = known.union(numbers)
# 과장된 이야기를 할 수 있는 파티 개수를 출력
print(sum(able))