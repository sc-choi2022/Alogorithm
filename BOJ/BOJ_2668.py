import sys

def dfs(n, path):
    for number in chart[n]:
        if number not in path:
            visit[number] = 1
            path.add(number)
            dfs(number, path.copy())
            visit[number] = 0
            path.remove(number)
        # 사이클을 이루는 경우
        else:
            results.update(path)
            return

# 표의 가로길이 N
N = int(sys.stdin.readline())
# 표의 내용을 저장하는 배열 chart
chart = [[] for _ in range(N+1)]

# 표의 번호와 아래 숫자를 저장
for i in range(1, N+1):
    chart[int(sys.stdin.readline())].append(i)

# 사이클 확인 여부를 저장하는 배열 visit
visit = [0] * (N+1)
# 사이클안에 들어가는 정수들을 저장하는 배열 result
results = set()

for j in range(1, N+1):
    if not visit[i]:
        visit[j] = 1
        dfs(j, {j,})

# 뽑힌 정수들의 개수를 출력
print(len(results))

# 뽑힌 정수들을 작은 수부터 큰 수의 순서로 한 줄에 하나씩 출력
results = sorted(list(results))
for result in results:
    print(result)