import sys

# 사람의 수 N, 파티의수 M
N, M = map(int, sys.stdin.readline().split())
known = set(sys.stdin.readline().rstrip().split()[1:])

party_lst = []
possible_lst = []

for _ in range(M):
    party_lst.append(set(sys.stdin.readline().rstrip().split()[1:]))
    possible_lst.append(1)

for _ in range(M):
    for idx, party in enumerate(party_lst):
        if known.intersection(party):
            possible_lst[idx] = 0
            known = known.union(party)

print(sum(possible_lst))