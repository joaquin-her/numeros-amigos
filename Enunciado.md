# Trabajo Práctico 0: Números Amigos

## Descripción del Problema

### ¿Qué son los Números Amigos?

Dos números son **amigos** cuando:
- La suma de los divisores del primero (excepto él mismo) es igual al segundo
- La suma de los divisores del segundo (excepto él mismo) es igual al primero

#### Ejemplo
Los números **220** y **284** son amigos:
- **Divisores de 220:** 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 y 110
  - Suma: 284
- **Divisores de 284:** 1, 2, 4, 71 y 142
  - Suma: 220

## Situación Actual

Se realizó un programa que calcula y muestra todos los pares de números amigos entre 1 y 100.000. 

### Problema de Eficiencia
- **Tiempo actual para 100.000:** 581 segundos (~10 minutos)
- **Tiempo estimado para 1.000.000:** más de 18 horas

## Objetivo del Trabajo

Diseñar e implementar mejoras al programa para que sea más eficiente.

> ⚠️ **IMPORTANTE:** NO SE DEBE DESARROLLAR UN NUEVO PROGRAMA NI CAMBIAR EL PROTOTIPO DE LA FUNCIÓN: sólo modificar el original.

## Requisitos de la Entrega

### 1. Supuestos
Identificar supuestos, limitaciones, condiciones o premisas bajo los cuales funcionará el algoritmo.

### 2. Análisis de Complejidad
Realizar un análisis de complejidad temporal del:
- Algoritmo actual
- Algoritmo propuesto

### 3. Tiempos de Ejecución
Medir y graficar los tiempos de ejecución para:
- 1 a 50.000
- 1 a 100.000
- 1 a 150.000
- 1 a 200.000
- 1 a 250.000
- (u otros intervalos relevantes)

### 4. Análisis de Resultados
Redactar un informe comparando los tiempos de ejecución.
- ¿Se corresponde con la complejidad temporal determinada inicialmente?
- Conclusiones

## Condiciones Generales de Entrega

### Modalidad
- **Tipo de trabajo:** Individual
- Se anima a discutir alternativas con compañeros, pero el desarrollo e implementación es individual

### Fecha Límite
- **22 de marzo a las 23:59** por campus
- Si no se entrega, se entrega fuera de plazo, o no funciona: **DESAPROBADO**

### Requisitos Técnicos
- **Python 3.10**
- Entregar un único archivo `.py` con formato: `TP0_Apellido_Padrón.py`
- La reingeniería debe ser transparente (no cambiar el prototipo de la función)

### Sistema de Bonificación
- **Los 10 mejores tiempos(*):** +1 en la nota final de los TPs (**)
- **Los 5 peores tiempos(*):** -1 en la nota final de los TPs

### Formato de Entrega
Archivo **ZIP** conteniendo:

1. **Documento PDF** con:
   - Carátula (nombre y padrón)
   - Índice
   - Numeración de páginas

2. **Código fuente** del algoritmo desarrollado
   - Incluir instrucciones para compilar (si es necesario) y ejecutar

3. **Archivo con resultados** obtenidos

### Política de Plagio
> ⚠️ **No se tolera el plagio**

Se pueden incluir citas siguiendo:
- Modelo propuesto por Rivas (2022) en el texto
- Listado completo en anexo usando normas APA 7ma edición

---

### Notas al Pie

(*) Los tiempos obtenidos en la computadora del profesor serán los únicos válidos para la evaluación

(**) No sirve para convertir un TP desaprobado en aprobado. La nota final de TP no puede ser mayor a 10