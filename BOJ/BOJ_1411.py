import sys

# 단어의 개수 N
N = int(sys.stdin.readline())
words = [sys.stdin.readline().strip() for _ in range(N)]
w_dic = {}
leng = len(words[0])

cnt = 0
for i in range(N):
    w1 = words[i]
    for j in range(i, N):
        w2 = words[j]
        w_dic = {}
        for l in range(leng):
            n1, n2 = w1[l], w2[l]
            if n1 in w_dic and w_dic[n1] != n2:
                break
            elif n1 in w_dic and w_dic[n1] == n2:
                continue
            else:
                w_dic[n1] = n2
    else:
        print(w1, w2)
        cnt += 1
print(cnt)