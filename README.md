# Numeros Amigos

Este repositorio busca resolver de manera algoritmica el problema de los numeros amigos que consiste en encontrar pares de numeros enteros positivos que cumplan que la suma de los divisores del primero (excepto él mismo) es igual al segundo, y la suma de los divisores del segundo (excepto él mismo) es igual al primero

Por ejemplo, los números 220 y 284 son amigos: 
- Los divisores de 220 son 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 y 110, y su suma es 284 
- Los divisores de 284 son 1, 2, 4, 71 y 142, que suman 220

## Descripción del Problema

El repositorio inicial provee un algoritmo de Fuerza Bruta que encuentra eficazmente pares de numeros amigos hasta un numero N, pero este algoritmo no es escalable debido a la exponencialidad temporal del mismo a mayor N. Por lo tanto, se busca una solución más eficiente que pueda encontrar pares de numeros en un menor tiempo, reingeniando el algoritmo original o utilizando otro método matemático.

## Algoritmo Original 

``` python
def amigos(MAX):
  
    for i in range(MAX): # O(n) 
        s=0
        for j in range (1,i-1+1): # O(n) 
            # Se buscan los divisores de i y se suman a s
            if i%j==0: # O(1)
                s+=j
        s2=0
        # Se buscan los divisores de s y se suman a s2
        for k in range (1,s-1):
            if s%k==0:
                s2+=k
        # Si s2 es igual a i, entonces i y s son amigos
        if i==s2:
            print(i,s)
    
amigos(100000)
```

### Analisis inicial
``` python
def amigos(MAX):
  
    for i in range(MAX): # O(n) 
        s=0
        for j in range (1,i-1+1): # O(n) 
            # Se buscan los divisores de i y se suman a s
            if i%j==0: # O(1)
                s+=j
        s2=0
        # Se buscan los divisores de s y se suman a s2
        for k in range (1,s-1): #O(n)
            if s%k==0:
                s2+=k
        # Si s2 es igual a i, entonces i y s son amigos
        if i==s2:
            print(i,s)
    
amigos(100000)
```
**Complejidad total temporal:** O(n^3)

**Complejidad total espacial:** O(1) 

Para realizar las pruebas del algoritmo mejorado y las mediciones comparativas al final, se insertaron los numeros amigos encontrados hasta 100.000 en un archivo `solucion.txt` seguido de la medicion del tiempo de ejecucion para ese valor.

## Instalacion 

``` bash
git clone https://github.com/joaquin-her/numeros-amigos.git
```
### Activacion entorno virtual:
``` bash
python -m venv .venv
source .venv/bin/activate
```
### Instalacion de requisitos
``` bash
pip install -r requirements.txt
```
## Ejecucion 
### Ejecucion algoritmo inicial:
``` bash
python old.py
```
### Ejecucion algoritmo optimizado:
``` bash
python main.py
```

## Pruebas
### Validacion de funcionamiento del algoritmo optimizado:
``` bash
pytest amigos_test.py
```

## Desarrollo de la solucion

Descrito en el informe [[informe/main.pdf]]