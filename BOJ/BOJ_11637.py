import sys

# 테스트 케이스의 수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 후보자의 수 N
    N = int(sys.stdin.readline())
    # 득표 수를 저장하는 배열 votes
    votes = [int(sys.stdin.readline()) for _ in range(N)]

    # 최다 득표자가 없을 경우
    if votes.count(max(votes)) > 1:
        print('no winner')
    # 최다 득표자가 과반수 들표를 했을 경우
    elif sum(votes)-max(votes) < max(votes):
        print(f'majority winner {votes.index(max(votes))+1}')
    # 최다 득표자가 절반 이하의 득표를 했을 경우
    else:
        print(f'minority winner {votes.index(max(votes))+1}')