n,m=map(int,input().split())
l=set(map(int,input().split()))
k=set(map(int,input().split()))
c=0
for i in l:
    if i  not in k:
        c+=1
for i in k:
    if i  not in l:
        c+=1
print(c)