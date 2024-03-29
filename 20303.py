import sys
input=sys.stdin.readline
n,m,k=map(int,input().split())
c=list(map(int,input().split()))
friend=[i for i in range(n+1)]

def find(friend,x):
    if x!=friend[x]:
        friend[x]=find(friend,friend[x])
    return friend[x]

def union(friend,a,b):
    rootA=find(friend,a)
    rootB=find(friend,b)
    if rootA<rootB:
        friend[rootB]=rootA
    elif rootA>rootB:
        friend[rootA]=rootB

for _ in range(m):
    a,b=map(int,input().split())
    union(friend,a,b)   

tmp=dict()
for i in range(n):
    root=find(friend,i+1)
    if root in tmp:
        tmp[root][0]+=c[i]
        tmp[root][1]+=1
    else:
        tmp[root]=[c[i],1]

steal=[]
for key,item in tmp.items():
    steal.append(item)

dp=[[0]*(k+1) for _ in range(len(steal)+1)]
for i in range(1,len(steal)+1):
    for j in range(1,k+1):
        if j<=steal[i-1][1]:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-steal[i-1][1]]+steal[i-1][0])
print(dp[-1][-1])