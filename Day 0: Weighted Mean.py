n=int(input())
lt=list(map(int,input().split(' ')))
lt2=list(map(int,input().split(' ')))
lt3=[]
for i in range(len(lt)):
    x=lt[i]*lt2[i]
    lt3.append(x)
weighted=sum(lt3)/sum(lt2)
print(round(weighted,1))


