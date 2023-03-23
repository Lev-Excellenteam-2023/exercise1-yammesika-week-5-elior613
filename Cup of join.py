def join(*l,sep='-'):
    new_list=[]
    if(not l): return None
    for i in l:
        new_list+=i
        if(l.index(i)!=len(l)-1):
            new_list+=sep
    return new_list
print(join([2,4],[8],sep='&'))

