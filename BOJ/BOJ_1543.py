import sys

# 문서 document
document = sys.stdin.readline().rstrip()
# 검색하고 싶은 단어 word
word = sys.stdin.readline().rstrip()

# 시작위치 idx 0
idx = 0

# 등장 횟수 cnt
cnt = 0

while idx < len(document):
    # word가 등장한 경우 cnt 1 증가 idx위치를 재설정
    if document[idx : idx + len(word)] == word:
        cnt += 1
        idx += len(word)
    # word가 등장하지 않은 경우 idx 1 증가
    else:
        idx += 1
# cnt 출력
print(cnt)