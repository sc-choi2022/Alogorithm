import sys

# 두문자 S와 T
S = sys.stdin.readline().rstrip()
T = sys.stdin.readline().rstrip()

while len(T) > len(S):
    # 문자열의 뒤에 A를 추가한 경우
    if T[-1] == 'A':
        T = T[:-1]
    # 문자열을 뒤집고 뒤에 B를 추가한 경우
    else:
        T = T[:-1][::-1]
# S를 T로 바꿀 수 있으면 1을 없으면 0을 출력
print(1 if T == S else 0)