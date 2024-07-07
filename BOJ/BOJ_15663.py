import sys

def dfs():
    return


# N개의 자연수 중에서 M개를 고르는 기준이 되는 자연수 N, M
N, M = map(int, sys.stdin.readline().split())
# N개의 자연수를 저장하는 배열 numbers
numbers = sorted(list(map(int, sys.stdin.readline().split())))
visit = [0]*N
# 만들어진 수열을 저장하는 셋 done
done = set()

dfs()