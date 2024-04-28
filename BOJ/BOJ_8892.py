import sys

# 테스트 케이스의 개수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 단어의 수 K
    K = int(sys.stdin.readline())
    # 단어들을 저장하는 배열 words
    words = [sys.stdin.readline().rstrip() for _ in range(K)]
    for i in range(K):
        # 팰린드롬을 만든 경우를 확인하는 변수 flag
        flag = False
        for j in range(i+1, K):
            w1 = words[i] + words[j]
            w2 = words[j] + words[i]
            if w1 == w1[::-1]:
                print(w1)
                flag = True
                break
            elif w2 == w2[::-1]:
                print(w2)
                flag = True
                break
        # 팰린드롬을 만든 경우
        if flag:
            break
    # 팰린드롬을 만들 수 없는 경우
    else:
        print(0)