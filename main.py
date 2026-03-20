import time
def amigos(MAX):
    sumas = []
    t1=time.time()
    for i in range(MAX):
        s=0
        for j in range (1,i-1+1):
            if i%j==0:
                s+=j
        sumas.append(s)
        if s > i:
            continue
        else:
            s2 = sumas[s]
            if i == s2:
                print(i,s)       
    t2=time.time()    
    print(t2-t1)
    
amigos(100000)