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

## **Uso**

Existen 3 opciones en el menu, las cuales se describen a continuacion.

### Opcion 1

La opción 1 del menu solicita ingresar el id de un aplicativo a mostrar.

**Ejemplo ejecucion:**
``` 
Ingrese el id de una aplicacion a buscar : 284666222
ID : 284666222
Nombre : pcalc - the best calculator
Tamano : 49250304 bytes
Precio : 9.99
User Rating : 4.5
Content Rating : 4+
Genero : Utilities
Vector Caracteristicas Normalizado: [0.006 0.066 1.35  0.    0.    0.    1.    0.    0.    0.    0.    0.
 0.    0.    0.    0.    0.    0.    0.    0.    0.    0.    0.    0.
 0.    0.    0.    0.    0.    1.   ]
```

### Opcion 2

La opción 2 del menu solicita el id de un aplicativo para el cual se buscaran 10 vecinos.
**Ejemplos ejecucion:**
``` 
Ingrese el id de una aplicacion a buscar : 284666222
Mostrando vecino numero 1
ID : 364738545
Nombre : filebrowser - access files on remote computers
Tamano : 68073472 bytes
Precio : 5.99
User Rating : 4.5
Content Rating : 4+
Genero : Utilities
Vector Caracteristicas Normalizado: [0.008 0.039 1.35  0.    0.    0.    1.    0.    0.    0.    0.    0.
 0.    1.    0.    0.    0.    0.    0.    0.    0.    0.    0.    0.
 0.    0.    0.    0.    0.    0.   ]
Mostrando vecino numero 2
ID : 499470113
Nombre : fileexplorer pro - file manager for computer nas
Tamano : 83620864 bytes
Precio : 4.99
User Rating : 4.5
Content Rating : 4+
Genero : Utilities
Vector Caracteristicas Normalizado: [0.01  0.033 1.35  0.    0.    0.    1.    0.    0.    0.    0.    0.
 0.    1.    0.    0.    0.    0.    0.    0.    0.    0.    0.    0.
 0.    0.    0.    0.    0.    0.   ]
 Y ASI SUCESIVAMENTE
```

### Opcion 3
La opción 3 solicita valores al usuario para construir internamente un vector de carácteristicas que posteriormente será normalizado y finalmente será pasado como parámetro al algoritmo KNN.

**Ejemplo ejecucion:**
``` 
Ingrese el tamano en bytes de su aplicativo : 100788224
Ingrese el precio en dolares de su aplicativo : 3.99
Ingrese el user rating de su aplicativo (Ej : 4.5) : 4.5
Opciones de Content Rating : 
1) 17+
2) 9+
3) 4+
4) 12+
Ingrese el content rating segun la opcion del menu : 3
Opciones de Genero : 
1) Navigation
2) Lifestyle
3) Education
4) Catalogs
5) Weather
6) Music
7) Games
8) Productivity
9) Business
10) News
11) Utilities
12) Travel
13) Photo & Video
14) Social Networking
15) Reference
16) Sports
17) Shopping
18) Food & Drink
19) Book
20) Health & Fitness
21) Medical
22) Entertainment
23) Finance
Ingrese el genero segun la opcion del menu : 7
Mostrando vecino numero 1
ID : 1039910808
Nombre : patchmania kids - a puzzle about bunny revenge!
Tamano : 102250496 bytes
Precio : 3.99
User Rating : 4.5
Content Rating : 4+
Genero : Games
Vector Caracteristicas Normalizado: [0.012 0.026 1.35  0.    0.    1.    0.    0.    0.    0.    0.    0.
 0.    1.    0.    0.    0.    0.    0.    0.    0.    0.    0.    0.
 0.    0.    0.    0.    0.    0.   ]
Mostrando vecino numero 2
ID : 477891975
Nombre : train drive ats
Tamano : 124789760 bytes
Precio : 3.99
User Rating : 4.5
Content Rating : 4+
Genero : Games
Vector Caracteristicas Normalizado: [0.015 0.026 1.35  0.    0.    1.    0.    0.    0.    0.    0.    0.
 0.    1.    0.    0.    0.    0.    0.    0.    0.    0.    0.    0.
 0.    0.    0.    0.    0.    0.   ]
 Y ASI SUCESIVAMENTE
```