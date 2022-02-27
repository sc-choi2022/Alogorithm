import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for case in range(1, T+1):
    # N개의 과목, 출력할 K의 과목
    N, K = map(int, input().split())
    # K개 과목의 점수합 최댓값 초기화
    ans = 0

    # N개 과목의 점수를 담은 리스트 scores
    scores = list(map(int, input().split()))
    # scores 정렬
    scores.sort()

    # 큰 순서대로 K개의 과목을 점수를 ans에 더해 정답을 할당
    for i in range(N-1, N-K-1, -1):
        ans += scores[i]

    # 테스트케이스 번호와 정답 출력
    print(f'#{case} {ans}')