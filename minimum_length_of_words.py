n=input()
s=n.split()
p=[]
for i in s:
    p.append(len(i))
print(min(p))