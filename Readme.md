# **Desafio 3**

Este repositorio considera la implementacion de un algoritmo KNN para la búsqueda de vecinos cercanos en un **KD Tree**.

## **Ejecución**
``` 
python3 main.py
```


## **Algoritmo Propuesto**

### **Vector de Caracteristicas**

Para el desarrollo de esta actividad se ha considerado inicialmente cargar los datos del archivo **csv** entregado en el enunciado de la tarea. Luego, se cargan todos los datos del archivo y se escogen únicamente los siguientes valores para armar el vector de caracteristicas.

- Size_Bytes
- Price
- User_Rating
- Cont_Rating
- Prime_Genre

### **Oneshot Encoding**

En el caso de los campos **Cont_Rating** y **Prime_Genre** al ser campos multivalor se utiliza la técnica de **OneShot Encoding** para transformar cada uno de sus datos en una representacion de un vector binario.

**Por ejemplo:**

| Genero |     Encoding      |
|----------|:-------------:|
| Music |  [1,0,0,0] |
| Sports |    [0,1,0,0]   |
| Lifestyle | [0,0,1,0]|
| Healthy | [0,0,0,1] |

### **Normalización**

Luego, al generar todos los vectores de características se procede a normalizar los vectores tomando como parámetro de normalización el máximo valor para los campos **Size_Bytes** , **Price** , **User_Rating** de forma individual. Esto quiere decir que de todos los vectores de características se escoge por ejemplo el máximo valor de **Size_Bytes** y se procede a dividir ese campo en todos los vectores de características por el máximo valor. De esta forma aseguramos que el valor de cada campo se mueve entre 0 y 1.

### **Ponderación**

Finalmente se realiza un proceso de ponderación de los datos, para agregar un mayor peso a algunos valores que consideramos más relevantes. Puntualmente se multiplic cada parámetro del vector normalizado según se muestra a continuación.


| Parámetro |     Factor      |
|----------|:-------------:|
| Size_Bytes |  0.5 |
| Price |    2.0   |
| User_Rating | 1.5|
| Oneshot Encoding | 1.0 |

### **Distancia**
Para el calculo de distancia entre dos vectores se utiliza la distancia euclideana.

## **Uso del Algoritmo**

El algoritmo inicialmente le solicita al usuario que escoja una de las 3 acciones propuestas. 

### ***Opción 1***
El usuario podrá ingresar un ID correspondiente a una APP en especifico, y podrá obtener todo el detalle relacionado a ella, como lo es su nombre, dicho ID, Size Bytes, etc. 
```
Ingrese el Id a buscar:
Id: 364740856
ID ENCONTRADO, APP NAME:Dictionary.com Dictionary & Thesaurus for iPad      
-----------------------------------------
1: Dictionary.com Dictionary & Thesaurus for iPad
ID: 364740856
Size Bytes:165748736
Currency: 0
Price: 4
Rating Count: 4+
Genero: Reference
[0.041 0.    0.9   0.    1.    0.    0.    1.    0.    0.    0.    0.       
 0.    0.    0.    0.    0.    0.    0.    0.    0.    0.    0.    0.       
 0.    0.    0.    0.    0.    0.   ]
-------------------------------------
```

### ***Opción 2***

A partir de un ID relacionado a una APP que será ingresado por el usuario, el algoritmo entregará la 10 aplicación más parecidas a ella de acuerdo a las características que esta contiene. En efecto:
```
Ingrese el Id a buscar:
Id: 687877464
ID ENCONTRADO, APP NAME:Stop - Fun Categories Word Game
-----------------------------------------
1: 暴风影音-BaoFeng Player
ID: 538248967
Size Bytes:83532800
Currency: 0
Price: 5.2.0
Rating Count: 17+
Genero: Entertainment
[0.026 0.    0.9   0.    1.    0.    0.    0.    1.    0.    0.    0.
 0.    0.    0.    0.    0.    0.    0.    0.    0.    0.    0.    0.
 0.    0.    0.    0.    0.    0.   ]
-------------------------------------
3: Zen Brush 2
ID: 1012274888
Size Bytes:69114880
Currency: 2.99
Price: 1.12
Rating Count: 4+
Genero: Entertainment
[0.026 0.    0.9   0.    1.    0.    0.    0.    1.    0.    0.    0.
 0.    0.    0.    0.    0.    0.    0.    0.    0.    0.    0.    0.
 0.    0.    0.    0.    0.    0.   ]
-------------------------------------
Y bajo el mismo formato, se presentarán las siguientes sugerencias.
```
### ***Opcion 3***

Análogo al punto 2, esta opcion entrega las características relacionadas a 10 app's que, a diferencia del punto anterior, aquí se define un set de caracteristicas propias por las cuales se desea tener información. En efecto.

```
Ingrese el tamano de bytes: 100788224
Ingrese un precio estimado: 3.99
Ingrese un rating estimado: 4.5
1) 12+
2) 4+
3) 17+
4) 9+
Ingrese el content rating segun la opcion del menu : 3
Opciones de Genero :
1) Reference
2) Sports
3) Lifestyle
4) Medical
5) Catalogs
6) Productivity
7) Food & Drink
8) Book
9) Photo & Video
10) Social Networking
11) Education
12) Travel
13) Weather
14) Finance
15) Utilities
16) Games
17) Health & Fitness
18) News
19) Music
20) Business
21) Shopping
22) Navigation
23) Entertainment
Ingrese el genero adecuado: 7
-----------------------------------------
1: ToonCamera
ID: 392538848
Size Bytes:29494272
Currency: 1.99
Price: 4
Rating Count: 4+
Genero: Photo & Video
[0.002 0.016 0.9   0.    0.    1.    0.    0.    0.    0.    0.    0.  0.    1.    0.    0.    0.    0.    0.    0.    0.    0.    0.    0.
 0.    0.    0.    0.    0.    0.   ]
-------------------------------------
2: BillMinder - Bill Reminder and Organizer
ID: 407262212
Size Bytes:4278742
Currency: 1.99
Price: 3.7.6
Rating Count: 4+
Genero: Finance
[0.002 0.016 0.9   0.    0.    1.    0.    0.    0.    0.    0.    0.  0.    1.    0.    0.    0.    0.    0.    0.    0.    0.    0.    0.
 0.    0.    0.    0.    0.    0.   ]
-------------------------------------
```

### ***Opcion 4*** 

Finalmente, a partir de un ID ingresado por el usuario, el algoritmo entrega los elementos más parecidos con el, sin embargo, los entrega realizando contrastes entre una lista con nodos y KD Tree. En efecto:
```
Ingrese el Id a buscar:
Id: 364740856
ID ENCONTRADO, APP NAME:Dictionary.com Dictionary & Thesaurus for iPad
INFORMACION USANDO KDD TREE
- Tiempo de busqueda estimado: 0.5465000000000001
- Cantidad de iteraciones: 82
INFORMACION USANDO LISTA
- Tiempo de busqueda estimado: 0.5499879
- Cantidad de iteraciones: 47
```

Si bien diferencia de tiempo es diferencial, se logra obtener que por medio de KDD Tree se realizan más cambios en comparación a las listas con nodos, sin embargo, esto puede ocurrir por la simplicidad que es escogido el nodo root del arbol, por lo cual, es un parámetro perfectible. Notar también que a pesar de todo, el arbol es recorrido completamente.