import time
import math
def amigos(MAX):
    sumas = {}
    t1=time.time()
    if MAX > 0:
        print(0, 0)
    # Calcular sumas de divisores usando el método de la criba
    for i in range(1, MAX):
        for j in range(i * 2, MAX + 1, i):
            sumas[j] = sumas.get(j, 0) + i
    
        s = sumas.get(i, 0)
        if s > i:
            continue
        else:
            if s in sumas:
                s2 = sumas[s]
                if i == s2:
                    print(i, s)       
    t2=time.time()    
    print(t2-t1)
    
amigos(200000)