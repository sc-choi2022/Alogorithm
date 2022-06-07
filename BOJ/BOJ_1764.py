# 듣도 못한 사람 수 N, 보도 못한 사람 수 M
N, M = map(int, input().split())

# 듣도 못한 사람이름을 담을 set listen
listen = set()

# 보도 못한 사람들이 listen에 있으면 이름을 담을 set look
look = set()

# 듣보잡의 수 cnt
cnt = 0

# N개의 듣도 못한 사람을 listen에 추가
for _ in range(N):
    listen.add(input())

# M개의 보도 못한 이름이 listen에 있다면 look에 추가
for _ in range(M):
    tmp = input()
    if tmp in listen:
        look.add(tmp)
        # look에 추가된 수 cnt에 반영위해 1 증가
        cnt += 1

# set을 list로 변경 후 sort로 사전순 정렬
look = list(look)
look.sort()

# 듣보잡의 수를 출력
print(cnt)
# 사전순으로 정렬된 look의 모든 l을 출력
for l in look:
    print(l)