import sys

# 테스트 케이스 개수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 카드의 개수 N
    N = int(sys.stdin.readline())
    # 카드에 적힌 알파벳을 저장하는 배열 alphabet
    alphabet = list(sys.stdin.readline().rstrip().split())

    answer = alphabet[0]
    for i in range(1, N):
        if alphabet[i] + answer < answer + alphabet[i]:
            answer = alphabet[i] + answer
        else:
            answer = answer + alphabet[i]
    # 만들 수 있는 문자열 중에서 사전 순으로 가장 빠른 문자열을 출력
    print(answer)