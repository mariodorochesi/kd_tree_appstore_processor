from typing import Set, Dict
from math import pow

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
    index : int = 1

    for item in categories:
        value = int(pow(10,categories_length-index))
        mapping[item] = value
        index +=1

    return mapping

def vectorize(size_byes, price, user_rating, cont_rating, prime_genre):
    '''
        Genera un Vector que contiene los siguientes datos.
        [Tamano , Precio , Rating Usuario , Rating Contenido, Genero]
    '''
    try:
        return [int(size_byes), float(price), float(user_rating), cont_rating, prime_genre]
    except:
        raise Exception('Error al convertir a Lista')