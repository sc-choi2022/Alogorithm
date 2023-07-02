import sys

# 사람의 수 N, 파티의수 M
N, M = map(int, sys.stdin.readline().split())
# 진실을 아는 사람의 수 K, 개수만큼의 사람들의 번호 known
known = set(sys.stdin.readline().rstrip().split()[1:])
# 과장된 이야기를 할 수 있는 파티의 여부를 저장하는 배열 check
able = [1]*M
# 각 파티 사람의 정보를 저장한 배열 parties
parties = [set(sys.stdin.readline().rstrip().split()[1:]) for _ in range(M)]
# 거짓말을 아는 사람들을 모두 확인하기 위한 for문
for _ in range(M):
    for idx, party in enumerate(parties):
        # 파티에 진실을 아는 사람이 있는 경우
        if known.intersection(parties[idx]):
            # 이야기를 할 수 없는 파티로 설정
            able[idx] = 0
            # 진실을 알게된 사람이 추가된다.
            known = known.union(parties[idx])

# 과장된 이야기를 할 수 있는 파티 개수를 출력
print(sum(able))