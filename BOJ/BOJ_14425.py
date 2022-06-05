# 집합 S에 포함된 문자열의 수 N과 주어지는 문자열의 수 M
N, M = map(int, input().split())
# 출력할 정답 cnt
cnt = 0
# S라는 집합을 생성
S = set()
# N개의 문자열을 S에 추가
for _ in range(N):
    S.add(input())

# M개의 문자열을 집합 S에 존재 여부를 확인하여 있다면 cnt 1 증가
for _ in range(M):
    string = input()
    if string in S:
        cnt += 1
# cnt를 출력
print(cnt)