import sys
from collections import defaultdict
# 영문자들을 담을 리스트 words
words = []
# 첫 영문자를 word에 저장
word = sys.stdin.readline().strip()

# word값이 '-'인 경우 break
while word != '-':
    # words에 word값 저장
    words.append(word)
    word = sys.stdin.readline().strip()

# 첫 퍼즐값을 board에 저장
board = list(sys.stdin.readline().strip())

# 확인할 퍼즐이 더이상 없는 경우 break
while board != ['#']:
    # default를 int값으로 가지는 b_dict 생성
    b_dict = defaultdict(int)
    # 퍼즐의 알파벳을 key값으로 b_dict에 저장

    # words의 각 단어에 대해
    for word in words:
        # 퍼즐의 알파벳으로 만들 수 있는 여부를 확인
        tmp = board[::]
        for w in word:
            if w in tmp:
                tmp.remove(w)
            else:
                break
        # 만들 수 있다면 중복은 제외하고 존재을 b_dict에 표시
        else:
            set_word = set(list(word))
            # 있는 경우 key 알파벳의 value 값 1 증가
            for w in set_word:
                b_dict[w] += 1
    # b_dict의 value중 가장 작은 값 minvalue, minvalue를 가지는 key들을 담은 리스트 minkeys
    minvalue = min(b_dict.values())
    minkeys = sorted(list(x for x in b_dict if b_dict[x] == minvalue))

    # b_dict의 value중 가장 큰 값 minvalue, maxvalue를 가지는 key들을 담은 리스트 maxkeys
    maxvalue = max(b_dict.values())
    maxkeys = sorted(list(x for x in b_dict if b_dict[x] == maxvalue))
    # 현재 board에 대해 조건에 맞게 출력
    print(''.join(minkeys), minvalue, ''.join(maxkeys), maxvalue)