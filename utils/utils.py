from typing import Set, Dict, List
from math import pow, trunc
import numpy as np
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def one_shot_encoding(categories : Set):
    '''
        Implementacion de OneShot Encoding.
        Retorna un diccionario con clave = clave y valor = encoding(clave)
    '''
    # Diccionario donde se mapea clave-encoding
    mapping : Dict = dict()
    # Tamanio de la lista de categorias
    categories_length : int  = len(categories)
    # Elementos procesados +1
    index : int = 0
    # Se genera una base de encriptacion
    base = '0' * categories_length

    for item in categories:
        value = base
        value = value[:index] + '1' + value[index + 1 :]
        mapping[item] = value
        index +=1

    return mapping

def vectorize(size_byes, price, user_rating, cont_rating, prime_genre):
    '''
        Genera un Vector que contiene los siguientes datos.
        [Tamano , Precio , Rating Usuario , Rating Contenido, Genero]
    '''
    try:
        vector = [int(size_byes), float(price), float(user_rating)]
        content_rating = [int(x) for x in str(cont_rating)]
        generes = [int(x) for x in str(prime_genre)]
        for i in content_rating:
            vector.append(i)
        for i in generes:
            vector.append(i)
        return vector
    except:
        raise Exception('Error al convertir a Lista')

def truncate(number, decimals=0):
    """
    Returns a value truncated to a specific number of decimal places.
    """
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer.")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more.")
    elif decimals == 0:
        return math.trunc(number)

    factor = 10.0 ** decimals
    return trunc(number * factor) / factor

def distance(vector_a  , vector_b):
    return np.linalg.norm(vector_a-vector_b)

def normalize(lista_vectores : List):
    '''
        Funcion para normalizar la lista de vectores. Para ello se normalizan
        en base a su maximo, los parametros tamano, precio y rating_usuario.
    '''
    lista_tamanos : List = list()
    lista_precio : List = list()
    lista_rating_usuario : List = list()

    for i in lista_vectores:
        lista_tamanos.append(i[0])
        lista_precio.append(i[1])
        lista_rating_usuario.append(i[2])

    maximo_tamanos = max(lista_tamanos)
    maximo_precio = max(lista_precio)
    maximo_rating_usuario = max(lista_rating_usuario)

    for i in lista_vectores:
        i[0] = truncate(0.5*i[0]/maximo_tamanos,3)
        i[1] = truncate(2*i[1]/maximo_precio,3)
        i[2] = truncate(1.5*i[2]/maximo_rating_usuario,3)

    for i in range(len(lista_vectores)):
        lista_vectores[i] = np.array(lista_vectores[i])

    return lista_vectores

def normalize_excluded(lista_vectores : List, vector):
    '''
        Metodo que normaliza un vector en base a una lista de vectores.
        Hace lo mismo del caso anterior pero no altera la lista de vectores,
        solamente altera el vector.
    '''
    lista_tamanos : List = list()
    lista_precio : List = list()
    lista_rating_usuario : List = list()

    for i in lista_vectores:
        lista_tamanos.append(i[0])
        lista_precio.append(i[1])
        lista_rating_usuario.append(i[2])

    maximo_tamanos = max(lista_tamanos)
    maximo_precio = max(lista_precio)
    maximo_rating_usuario = max(lista_rating_usuario)
    vector[0] = truncate(0.5 * (vector[0]/maximo_tamanos),3)
    vector[1] = truncate(2 * vector[1]/maximo_precio, 3)
    vector[2] = truncate(1.5 * vector[2]/maximo_rating_usuario, 3)

    return vector

def menu():
    cls()
    print('Seleccione una de las opciones disponibles.')
    print('1.- Mostrar informacion de una aplicacion en especifico.')
    print('2.- Mostrar informacion de 10 aplicaciones mas parecidas a una dada por id.')
    print('3.- Mostrar informacion de 10 aplicaciones mas parecidas segun vector.')
    print('0.- Cerrar programa.')