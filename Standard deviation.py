n=int(input())
lt=list(map(int,input().split(' ')))
s=sum(lt)
lt2,lt3=[],[]
m=s//n
for i in lt:
    x=abs(i-m)
    lt2.append(x)
for i in lt2:
    sq=i**2
    lt3.append(sq)
su=sum(lt3)
ans=(su/n)**0.5
print(ans)
