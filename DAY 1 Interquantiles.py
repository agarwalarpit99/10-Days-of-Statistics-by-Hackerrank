n=int(input())
lt=list(map(int,input().split(' ')))
dic={}
lt2=[]
freq=list(map(int,input().split(' ')))
for i in range(len(lt)):
    dic[lt[i]]=freq[i]
for i,j in dic.items():
    x=j
    for k in range(j):
        lt2.append(i)
lt2.sort()
if len(lt2)%2!=0:
    lodd=len(lt2)//2
    print(float(lt2[lodd]))
else:
    r=len(lt2)//2
    lower=lt2[:r]
    upper=lt2[r:]
#print(upper)
#print(lower)
    l=len(lower)//2
    l2=len(upper)//2

    if len(lower)%2==0:
        q1=(lower[l]+lower[l-1])//2
    else:
        q1=lower[l2]
    if len(upper)%2==0:
        q2=(upper[l2]+upper[l2-1])//2
    else:
        q2=upper[l2]
    print(float(q2-q1))
