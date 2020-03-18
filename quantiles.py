n=int(input())
lt=list(map(int,input().split(' ')))
q2=0
q1,q3=0,0
lt1,lt2=[],[]
lt.sort()
if n%2==0:
    l2=n//2
    q2=(lt[l2]+lt[l2-1])//2
    lt1=lt[:l2]
    lt2=lt[l2:]
    if len(lt1)%2==0:
        l1=len(lt1)//2
        q1=(lt1[l1]+lt1[l1-1])//2
    elif len(lt1)%2!=0:
        l1=len(lt1)//2
        q1=lt1[l1]
    if len(lt2)%2==0:
        l2=len(lt2)//2
        q3=(lt2[l2]+lt2[l2-1])//2
    elif len(lt2)%2!=0:
        l2=len(lt2)//2
        q3=lt2[l2]

    
else:
    l=n//2
    q2=lt[l]
    lt1=lt[:l]
    lt2=lt[l+1:]
    l1=len(lt1)//2
    q1=(lt1[l1]+lt1[l1-1])//2
    l3=len(lt2)//2
    q3=(lt2[l3]+lt2[l3-1])//2

'''print(lt)
print(lt1)
print(lt2)'''
print(q1)
print(q2)
print(q3)
