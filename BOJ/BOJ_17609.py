import sys

# 유사회문여부를 확인하는 함수 maybePalindrome
def maybePalindrome(word, left, right):
    while left < right:
        # 유사회문이 아닌 경우 False return
        if word[left] != word[right]:
            return False
        else:
            left += 1
            right -= 1
    # 유사회문인 경우 True return
    return True

def isPalindrome(word, left, right):
    # 회문인 경우 0 return
    if word == word[::-1]:
        return 0
    while left < right:
        # 회문이 아닌 경우 유사회문을 확인
        if word[left] != word[right]:
            checkLeft = maybePalindrome(word, left+1, right)
            checkRight = maybePalindrome(word, left, right-1)
            # 유사회문의 값이 True인 경우 1 return
            if checkLeft or checkRight:
                return 1
            # 유사회문의 값이 False인 경우 2 return
            else:
                return 2
        else:
            left += 1
            right -= 1

# 문자열의 개수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 문자열 word
    word = sys.stdin.readline().rstrip()
    # 함수 isPalindrome의 return 값인 회문여부를 출력
    print(isPalindrome(word, 0, len(word)-1))