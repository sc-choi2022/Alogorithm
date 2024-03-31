import sys

def dfs(depth, prev):
    global minN, maxN
    if depth == K:
        tmp = ''.join(numbers)
        if tmp > maxN:
            maxN = tmp
        if tmp < minN:
            minN = tmp
        return
    if inequality[depth] == '<':
        for j in range(9+1):
            if prev < j and not visit[j]:
                visit[j] = 1
                numbers[depth+1] = str(j)
                dfs(depth+1, j)
                visit[j] = 0
    else:
        for j in range(9, -1, -1):
            if prev > j and not visit[j]:
                visit[j] = 1
                numbers[depth+1] = str(j)
                dfs(depth+1, j)
                visit[j] = 0

# 부등호 문자의 개수 K
K = int(sys.stdin.readline())
# 부등호를 저장하는 배열 inequality
inequality = list(sys.stdin.readline().rstrip().split())
# 사용한 숫자 여부를 저장하는 배열 visit
visit = [0]*10
# 사용한 숫자를 저장하는 배열 numbers
numbers = ['0']*(K+1)
# 부등호 관계를 만족하는 최솟값 minN, 최댓값 maxN
minN, maxN = '9'*(K+1), '0'*(K+1)

for i in range(9+1):
    visit[i] = 1
    numbers[0] = str(i)
    dfs(0, i)
    visit[i] = 0

# 제시된 부등호 관계를 만족하는 k+1 자리의 최대, 최소 정수를 첫째 줄과 둘째 줄에 각각 출력
print(maxN)
print(minN)