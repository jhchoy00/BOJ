import sys
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
dp=[1]*(n+1)
for i in range(1,n+1):
    for j in range(i-1):
        if a[j]<a[i-1]:
            dp[i]=max(dp[i],dp[j+1]+1)
print(max(dp))