import sys

# 단어의 개수 N
N = int(sys.stdin.readline())
# 모든 단어를 담을 리스트 words
words = [sys.stdin.readline().strip() for _ in range(N)]
# 바꾸는 알파벳 정보를 담을 딕셔너리 w_dic
w_dic = {}
# 단어의 길이 leng
leng = len(words[0])
# 출력할 쌍의 개수 cnt
cnt = 0

for i in range(N):
    w1 = words[i]
    for j in range(i+1, N):
        w2 = words[j]
        # 딕셔너리 w_dic 초기화
        w_dic = {}
        for l in range(leng):
            n1, n2 = w1[l], w2[l]
            # w_dic에 key n1 존재하는 경우
            if n1 in w_dic:
                # 기존과 다른 알파벳으로 교환해야하는 경우 break
                if w_dic[n1] != n2:
                    break
            # w_dic에 key n1 존재하지 않는 경우
            else:
                # key n1이 존재하지 않으나 n2이 value로 존재한다면 break
                if n2 in w_dic.values():
                    break
                else:
                    # w_dic에 key는 n1, value는 n2로 저장
                    w_dic[n1] = n2
        # 숌스러운 쌍인 경우
        else:
            # cnt 1 증가
            cnt += 1
# cnt 출력
print(cnt)