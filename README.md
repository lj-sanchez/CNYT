# Librería de Complejos

#### La librería contiene las siguientes operaciones:

  1. Suma </p>
  2. Multiplicación </p>
  3. Resta </p>
  4. División </p>
  5. Módulo </p>
  6. Conjugado </p>
  7. Conversión entre representaciones polar y cartesiano </p>
  8. Fase de un número complejo </p>
 
#### La librería está terminada, teniendo encuenta que son ocho operaciones básicas de números complejos.
 A continuación se mostrará el código de cada operación:
 1. Suma. Para esta operación es necesario sumar las dos partes reales y luego las dos partes imaginarias.
```
def sumacplx(c1,c2):
    real = c1[0] + c2[0]
    ima = c1[1] + c2[1]
    resul = (real,ima)
    return resul
```
2. Multiplicación. Esta operación está definida como: (a1*a2-b1*b2, a1*b2+a2*b1) siendo c1=(a1,b1) y c2=(a2,b2).   
```
def multcplx(c1,c2):
    real = (c1[0]*c2[0]) - (c1[1]*c2[1])
    ima = (c1[0]*c2[1]) + (c2[0]*c1[1])
    resul = (real,ima)
    return resul
```
3. Resta. Para esta operación es necesario restar las dos partes reales y luego las dos partes imaginarias.
```
def rescplx(c1,c2):
    real = c1[0] - c2[0]
    ima = c1[1] - c2[1]
    resul = (real,ima)
    return resul
```
4. División. En esta operación se multiplica numerador y denominador por el conjugado del denominador y se realizan las operaciones correspondientes.
```
def divcplx(c1,c2):
    den = c2[0]**2 + c2[1]**2
    x = c1[0]*c2[0] + c1[1]*c2[1]
    y = c2[0]*c1[1] - c1[0]*c2[1]
    resul = (x/den, y/den)
    return resul
```
5. Módulo. Esta operación es para un solo número complejo y se obtiene realizando la suma de los cuadrados de la parte real e imaginaria, y luego se realiza la raíz cuadrada.  
```
def moducplx(c):
    mod = round(math.sqrt(c[0]**2 + c[1]**2),2)
    return mod
```
6. Conjugado. Esta operación niega solo el signo de la parte imaginaria del número complejo.
```
def conjugado(c):
    return (c[0],-c[1])
```
7.1 Polar a cartesiano. En esta operación se tiene un número en coordenadas polares (p,θ), y para pasarlo a coordenadas cartesianas se halla la parte real multiplicando p por el coseno del ángulo, y para la parte imaginaria se multiplica p por el seno del ángulo.
```
def polycar(c):
    real = round(c[0]*math.cos(c[1]),2)
    ima = round(c[0]*math.sin(c[1]),2)
    resul = (real, ima)
    return resul
```
7.2 Cartesiano a polar. En esta operación se tiene un número complejo dado en coordenadas cartesianas, para hallar el número en coordenadas polares (p,θ), p se halla sumando los cuadrados del número complejo y luego se realiza la raíz cuadrada, y para el ángulo θ se utiliza el arcotangente de la división de la parte imaginaria del número complejo sobre la parte real.
```
def carypol(c):
    magp = round(math.sqrt(c[0]**2 + c[1]**2),2)
    fase = round(fasecplx(c),2)
    resul = (magp, fase)
    return resul
```
8. Fase.
```
def fasecplx(c):
    fase = round(math.degrees(math.atan(c[1]/c[0])),2)
    return fase
```

#### En esta plataforma se incluye una librería con ocho operaciones de los números complejos, y además un archivo con pruebas para cada operación.

Hecho por Lina Sánchez.
