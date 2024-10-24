from collections import defaultdict
import sys

# 참가자 명수 N, 장르의 개수 M, 본선 진출 명수 K
N, M, K = map(int, sys.stdin.readline().split())
# 참가자의 최대 능력을 저장하는 딕셔너리 talent
talent = defaultdict(int)

for _ in range(M):
    score = list(map(float, sys.stdin.readline().split()))
    # 참가자의 최대 능력치를 갱신
    for i in range(0, N, 2):
        talent[score[i]] = max(talent[score[i]], score[i+1])
# 각 참가자의 최대 능력치를 정렬
answer = sorted(list(talent.values()), reverse=True)

# 본선 참가자 K명의 능력의 합을 소수점 첫째자리까지 반올림해 출력
print(round(sum(answer[:K]), 2))