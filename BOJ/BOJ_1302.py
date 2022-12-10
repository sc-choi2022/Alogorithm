import sys

# 책의 개수 N
N = int(sys.stdin.readline())

# 책의 제목의 팔린 횟수를 담을 딕셔터리 titles
titles = {}

for _ in range(N):
    # 팔린 책의 제목 title
    title = sys.stdin.readline().rstrip()

    # title이 이미 titles에 존재
    if title in titles:
        # 팔린 횟수 1 증가
        titles[title] += 1
    else:
        # titles에 title 추가
        titles[title] = 1
# titles를 팔린 횟수가 많은 순서로 정렬하고 횟수가 동일하다면 제목을 이름순으로 정렬
titles = sorted(titles.items(), key = lambda x : (-x[1], x[0]))

# 가장 많이 팔린 책의 제목을 출력
# 가장 많이 팔린 책이 여러 개일 경우에는 사전 순으로 가장 앞서는 제목을 출력
print(titles[0][0])