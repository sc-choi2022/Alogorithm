# 응시자의 수 N, 상을 받는 사람의 수 k
N, k = map(int, input().split())

# 학생들의 점수
x = sorted(list(map(int, input().split())), reverse=True)
# 상을 받는 커트라인 점수를 출력
print(x[k-1])