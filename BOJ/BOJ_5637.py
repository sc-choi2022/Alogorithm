import re

# 입력 S
S = re.findall('[A-Z\-a-z]+', open(0).read()[:-1])
S.sort(key=lambda x: len(x), reverse=True)

# 가장 긴 단어를 소문자로 출력
print(S[0].lower())