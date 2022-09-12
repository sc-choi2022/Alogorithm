# 수열 A의 크기 N
N = int(input())
# 수열 A
A = list(map(int, input().split()))
# 감소하는 부분수열을 구하기 위해 reverse된 수열 AA
AA = A[::-1]
# 증가하는 부분수열의 각 위치를 포함한 길이를 담을 리스트 increase
increase = [1] * N
# 감소하는 부분수열의 각 위치를 포함한 길이를 담을 리스트 decrease
decrease = [1] * N

for i in range(N):
    for j in range(i):
        # A[i] > A[j]인 경우, 즉 증가하는 부분수열이 가능한 경우
        if A[i] > A[j]:
            # increase[i]의 값을 기존 값과 increase[j]+1의 값 중 큰 값으로 저장
            increase[i] = max(increase[i], increase[j]+1)
        # AA[i] > AA[j]인 경우, 즉 감소하는 부분수열이 가능한 경우
        if AA[i] > AA[j]:
            # decrease[i]의 값을 기존 값과 decrease[j]+1의 값 중 큰 값으로 저장
            decrease[i] = max(decrease[i], decrease[j]+1)
# 각 인덱스를 가장 큰 값으로 하는 부분수열의 길이를 담을 리스트 result
result = [0]*N
# increase와 decrease의 인덱스를 맞춰 더하기 위해 decrease를 reverse
decrease = decrease[::-1]

for k in range(N):
    # result[i]에 increase[i]와 decrease[i]을 더하고 각 위치가 중복으로 세어졌기 때문에 값에 -1하여 저장
    result[k] = increase[k] + decrease[k] - 1
# A의 부분 수열 중에서 가장 긴 바이토닉 수열의 길이를 출력
print(max(result))