n=int(input())
l=list(map(int,input().split()))
c=0
s=0
for i in range(0,n//2,1):
    c+=l[i]
for i in range(n//2,n,1):
    s+=l[i]
print(c)
print(s)