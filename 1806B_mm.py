import sys
import heapq
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    arr = list(map(int,input().split()))

    zero_count = 0
    one_count = 0

    for el in arr:
        if el == 0: zero_count += 1
        elif el == 1: one_count += 1

    if N % 2 == 0: zeropos = N // 2
    else : zeropos = N // 2 + 1

    if zero_count == N : print(1)

    elif zero_count <= zeropos:
        print(0)
        
    else :
        if one_count + zero_count == N:
            print(2)           
        else :
            print(1)