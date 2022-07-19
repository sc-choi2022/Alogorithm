import sys
# 사람의 수 N
N = int(sys.stdin.readline())
# 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 담간 리스트 P
P = list(map(int, sys.stdin.readline().split()))
# 시간이 짧게 걸리는 사람부터 일을 처리하면 기다리는 시간이 줄어든다.
# 따라서 sort를 통해 P을 정렬시킨다.
P.sort()
# 앞 사람의 시간만큼 기다려야하는 것이므로 각 사람이 돈을 뽑는데까지 걸리는 시간을 담아준다.
for i in range(1, len(P)):
    P[i] = P[i-1] + P[i]
# 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 출력한다.
print(sum(P))