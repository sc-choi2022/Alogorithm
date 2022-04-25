score = list(map(int, input()))     # N의 각 자리수를 담은 리스트 score
L = len(score)                      # N의 자릿수 L
s1 = sum(score[:L//2])              # L//2를 기준으로 왼쪽 부분의 각 자릿수의 합 s1
s2 = sum(score[L//2:])              # L//2를 기준으로 오른쪽 부분의 각 자릿수의 합 s2
if s1 == s2:
    print('LUCKY')                  # s1와 s2가 같은 값이면 LUCKY 출력
else:
    print('READY')                  # 아닌 경우 READY 출력