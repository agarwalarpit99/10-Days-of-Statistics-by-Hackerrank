n=int(input())
lt=list(map(int,input().split(' ')))
s=sum(lt)
l=len(lt)
print(s/l)
#print(lt)
lt.sort()
dic=dict()
if l%2==0:
    m=l//2
    n=m-1
    median=(lt[m]+lt[n])/2
else:
    m=l//2
    median=lt[m]/2
print(median)
lt2=[]
for i in range(l):
    x=lt[i]
    c=lt.count(x)
    lt2.append(c)
    dic[x]=c
mn=max(lt2)
lt3=[]
for k,v in dic.items():
    if v==mn:
        lt3.append(k)
print(min(lt3))
