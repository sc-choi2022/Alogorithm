import sys

# 펠린드롬 여부를 확인하는 recur 함수
def recur(s, l, r):
    global cnt
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        cnt += 1
        return recur(s, l + 1, r - 1)

# 펠린드롬 여부를 확인하는 recur 함수를 실행하는 함수 isPalindrome
def isPalindrome(s):
    return recur(s, 0, len(s) - 1)

# 테스트케이스의 개수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 알파벳 대문자로 구성된 문자열 S
    S = sys.stdin.readline().strip()
    # recursion 함수의 호출 횟수 cnt을 1로 초기화
    cnt = 1

    # isPalindrome 함수의 반환값과 recursion 함수의 호출 횟수를 한 줄에 공백으로 구분하여 출력
    print(isPalindrome(S), cnt)