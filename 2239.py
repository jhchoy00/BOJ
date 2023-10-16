import sys
input=sys.stdin.readline
a=[[0]*10 for _ in range(10)]
c=[[False]*10 for _ in range(10)]
c2=[[False]*10 for _ in range(10)]
c3=[[False]*10 for _ in range(10)]
n=9
cnt=0

def square(x, y):
    return (x//3)*3+(y//3)

def go(z):
    global cnt
    cnt += 1
    if cnt >= 10000000:
        return True
    
    if z == 81:
        for i in range(n):
            for j in range(n):
                print(a[i][j],end='')
            print()
        return True
    
    x = z//n
    y = z%n
    if a[x][y] != 0:
        return go(z+1)
    else: 
        for i in range(1,10):        
            if not c[x][i] and not c2[y][i] and not c3[square(x,y)][i]: 
                c[x][i] = c2[y][i] = c3[square(x,y)][i] = True
                a[x][y] = i
                if (go(z+1)): 
                    return True               
                a[x][y] = 0
                c[x][i] = c2[y][i] = c3[square(x,y)][i] = False
    return False

for i in range(9):
    tmp=input().rstrip()
    for j in range(9):
        tj=int(tmp[j])
        if tj!=0:
            a[i][j]=tj
            c[i][tj]=True
            c2[j][tj]=True
            c3[square(i,j)][tj]=True

go(0)