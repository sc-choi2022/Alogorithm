import sys

# 팀의 수 N, 카약이 손상된 팀의 수 S, 카약을 하나 더 가져온 팀의 수 R
N, S, R = map(int, sys.stdin.readline().split())
# 카약이 손상된 팀의 번호를 저장하는 배열 broken
broken = set(map(int, sys.stdin.readline().split()))
# 카약을 하나 더 가져온 팀의 번호를 저장하는 배열 spare
spare = set(map(int, sys.stdin.readline().split()))

# 카약이 손상되었지만 하나 더 가져온 팀을 broken과 spare에서 제외
intersection = broken&spare
broken = broken-intersection
spare = sorted(list(spare-intersection))

# 카약을 빌릴 수 있는 팀을 broken에서 제외
for s in spare:
    if s-1 in broken:
        broken.remove(s-1)
    elif s+1 in broken:
        broken.remove(s+1)

# 출발을 할 수 없는 팀의 최솟값을 출력
print(len(broken))