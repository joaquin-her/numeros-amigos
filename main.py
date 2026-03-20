import time
import math
def amigos(MAX):
    sumas = [0] * MAX
    t1=time.time()
    for i in range(MAX):
        sumas[i] = suma_de_divisores(i)
        s = sumas[i]
        if s > i:
            continue
        else:
            if s < MAX:
                s2 = sumas[s]
                if i == s2:
                    print(i,s)       
    t2=time.time()    
    print(t2-t1)
    
def suma_de_divisores(numero):
    if numero <= 1:
        return 0
    suma = 1  # 1 siempre es divisor
    sqrt_n = int(math.sqrt(numero))
    
    for i in range(2, sqrt_n + 1):
        if numero % i == 0:
            suma += i
            if i != numero // i:  # Evitar contar dos veces el mismo divisor
                suma += numero // i
    
    return suma
amigos(100000)