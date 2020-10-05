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
