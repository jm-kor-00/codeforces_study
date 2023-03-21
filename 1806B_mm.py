import sys
import heapq
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    arr = list(map(int,input().split()))
    array = []; inArr = [0,0]
    for i in range(N-1):
        heapq.heappush(array,arr[i]+arr[i+1])
    
    initial = heapq.heappop(array)
    if initial > 0 :
        print(initial - 1);continue
    
    for i in range(N - 2):
        tmp  = heapq.heappop(array)
        if inArr[1] + 1 < tmp: break
    print(inArr[1] + 1)