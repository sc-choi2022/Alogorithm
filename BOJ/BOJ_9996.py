import sys

def check():
    # 파일이름 file
    file = sys.stdin.readline().rstrip()
    # words의 두 문자열의 길이를 prefix, sufix으로 저장
    prefix = len(words[0])
    suffix = len(words[1])
    # 파일이름의 길이로 인해 불가능한 경우
    if prefix + suffix > len(file):
        return 'NE'
    # 일치하지 않는 경우
    if file[:prefix] != words[0] or file[-suffix:] != words[1]:
        return 'NE'
    return 'DA'

# 파일의 개수 N
N = int(sys.stdin.readline())
# 패턴 문자열 pattern
pattern = sys.stdin.readline().rstrip()
# *을 기준으로 나눈 패턴 문자열을 저장하는 배열 words
words = pattern.split('*')

# 입력으로 주어진 i번째 파일 이름이 패턴과 일치하면 "DA", 일치하지 않으면 "NE"를 출력
for _ in range(N):
    print(check())