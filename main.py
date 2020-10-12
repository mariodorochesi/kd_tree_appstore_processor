# -*- coding: utf-8 -*-
from typing import List, Dict, Set
from utils.utils import one_shot_encoding, vectorize, normalize, distance
from kd_tree.KD_Tree import KD_Tree, KD_Node
import sys
# Declaracion de Constantes
ARCHIVO = 'datos.csv'

if __name__ == "__main__":

    # Se hace la lectura del archivo
    archivo_datos = open(ARCHIVO, 'r', encoding='utf8')
    # Conjunto de Generos
    conjunto_generos : Set = set()
    # Conjunto de Content Ratings
    conjunto_content_rating : Set = set()
    # Diccinario con correlativo ID:Trackname
    diccionario_ids_name : Dict = dict()
    # Skip a la primera linea
    archivo_datos.readline()
    '''
        Se hace un procesamiento inicial del texto para generar:
            - Diccionario con ID:Trackname
            - Conjunto de Generos
            - Conjunto de Content Rating
    '''
    for linea in archivo_datos:
        '''
            0 : Numeral
            1 : Id
            2 : Track Name
            3 : size_bytes
            4 : currency
            5 : price
            6 : rating_count_tot
            7 : rating_count_ver
            8 : user_rating
            9 : user_rating_ver
            10 : ver
            11 : cont_rating
            12 : prime_genre
            13 : sup_devices.num
            14 : ipadSc_urls.num
            15 : lang.num
            16 : vpp_lic
        '''
        linea = linea.strip().split(',')
        # Se hace un mapeo id : nombre
        diccionario_ids_name[linea[1]] = linea[2]
        # Se agrega el genero a un conjunto
        conjunto_generos.add(linea[12])
        # Se agrega el content rating a un conjunto
        conjunto_content_rating.add(linea[11])
    # Se obtiene un diccionario de Generos Codificados con OneShot Encoding
    diccionario_generos_codificados = one_shot_encoding(conjunto_generos)
    # Se obtiene un dicciionario de Content Rating codificados con OneShot Encoding
    diccionario_content_rating = one_shot_encoding(conjunto_content_rating)
    # Se hace un rewind al archivo.
    archivo_datos.seek(0)
    # Skip primera linea
    archivo_datos.readline()
    # Contador de lineas
    contador_lineas = 0
    # Conjunto de vectores
    lista_vectores : List = list()
    lista_ids : List = list()
    
    # Nodes
    lista_nodes : List= list()

    for linea in archivo_datos:
        '''
            0 : Numeral
            1 : Id
            2 : Track Name
            3 : size_bytes
            4 : currency
            5 : price
            6 : rating_count_tot
            7 : rating_count_ver
            8 : user_rating
            9 : user_rating_ver
            10 : ver
            11 : cont_rating
            12 : prime_genre
            13 : sup_devices.num
            14 : ipadSc_urls.num
            15 : lang.num
            16 : vpp_lic
        '''
        linea = linea.strip().split(',')
        # Se obtiene el vector utilizando la funcion vectorize definida en utils.py
        vector = vectorize(linea[3], linea[5], linea[8], 
                        diccionario_content_rating.get(linea[11]),
                        diccionario_generos_codificados.get(linea[12]))
        lista_vectores.append(vector)
        lista_ids.append(linea[1])
        contador_lineas +=1
        
    # Se obtiene una Lista Normalizada de np.arrays
    lista_vectores = normalize(lista_vectores)
    root = KD_Node(lista_vectores.pop(), 0, 0)
    
    tree = KD_Tree(root)
    id = 0
    node = KD_Node(lista_vectores[10], 9, 2)
    
    node2 = KD_Node(lista_vectores[11], 8, 3)
    node3 = KD_Node(lista_vectores[12], 7, 4)
    node4 = KD_Node(lista_vectores[13], 6, 5)
    '''
    
    print(root.vector)
    tree.buildTree(root,node)
    tree.buildTree(root,node2)
    tree.buildTree(root,node3)
    tree.buildTree(root,node4)

    tree.printTree(root)
    '''
    
    for n in lista_vectores:
        node = KD_Node(n, id, id)
        tree.buildTree(root,node)
        id+=1

    
    tree.KNN(root,10)
    
