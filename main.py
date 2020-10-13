# -*- coding: utf-8 -*-
from typing import List, Dict, Set
from utils.utils import one_shot_encoding, vectorize, normalize, distance, normalize_excluded
from kd_tree.KD_Tree import KD_Tree, KD_Node
import sys
import copy as cp
# Declaracion de Constantes
ARCHIVO = 'datos.csv'

def printInstruccion():
    print("HOLA, ¿QUE ES LO QUE TE GUSTARÍA BUSCAR?")
    print("1- Informacion de una aplicacion")
    print("2- Informacion sobre 10 aplicaciones más parecidas a otra")
    print("3- Informacion sobre 10 aplicaciones más parecidas respecto a unos atributos")
    print("Presiona 0 para salir")

def searchById(lista_vectores, dictName):
    accept = True
    index = 0
    
    while(accept):
        print("Ingrese el Id a buscar:")
        id = int(input("Id: "))
        name = None
        count = 0

        for v in dictName.keys():
            if(id == int(v)):
                accept = False
                name = dictName[v]
                index = count
            count+=1

        if(name is None):
            print("ID no valido, ingreselo nuevamente") 
    
    print("ID ENCONTRADO, APP NAME:"+name)
    return KD_Node(lista_vectores[index],id)
        

def searchGroupByCart():
    tamByt = int(input("Ingrese el tamano de bytes: "))
    precio = float(input("Ingrese un precio estimado: "))
    user_rating = float(input("Ingrese un rating estimado: "))
    
    count = 0
    for i in diccionario_content_rating.keys():
        count = count + 1
        print(f"{count}) {i}")
    
    cont_rating = int(input("Ingrese el content rating segun la opcion del menu : "))
    
    print("Opciones de Genero : ")
    # Se despliegan las opciones de Generos
    count = 0
    for i in diccionario_generos_codificados.keys():
        count = count + 1
        print(f"{count}) {i}")
    
    genero = int(input("Ingrese el genero adecuado: "))

    cont_rating = diccionario_content_rating[list(diccionario_content_rating.keys())[cont_rating-1]]
    
    genero = diccionario_generos_codificados[list(diccionario_generos_codificados.keys())[genero-1]]

    vector = vectorize(tamByt, precio, user_rating, cont_rating, genero)
    
    vector = normalize_excluded(lista_vectores_no_normalizados, vector)

    final = KD_Node(vector, len(vector))
    return final

def printSimilars():
    count = 0
    element = []
    for s in similar:
        count+=1 
        element = returnCodName(s.id)
        print("Similitud n"+str(count)+": "+ element[1] )
        
def returnCodName(id):
    index = 0
    for i in diccionario_ids_name.keys():
        if(index == id):
            return [i,diccionario_ids_name[i]]    
        index +=1 



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
    # Index idLine - idName
    translateId: Dict = dict()

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
        
    ########################### COMIENZA EL MENU
    print(len(lista_vectores))
    printInstruccion()
    running = True
    nKNN = 0
    similar = []

    # Se obtiene una Lista Normalizada de np.arrays
    lista_vectores_no_normalizados = cp.deepcopy(lista_vectores)
    lista_vectores = normalize(lista_vectores)
    root = KD_Node(lista_vectores.pop(),0)
    
    #Se crea el Arbol KD
    tree = KD_Tree(root)

    id = 1
    for n in lista_vectores:
        node = KD_Node(n,id)
        tree.buildTree(node)
        id+=1
    
    while(running):
        option = int(input("Opcion "))
    
        while(option < 0 or option > 3):
            print("Opcion no aceptada, intente nuevamente")
            option = int(input("Opcion "))
        
        if(option == 0):
            running = False
            print("Muchas gracias por preferirnos")
            sys.exit(-1)

        elif(option == 1):
            #POR ID
            nKNN = 1
            toSearch = searchById(lista_vectores, diccionario_ids_name)
            similar = tree.KNN(toSearch,nKNN)

        elif(option == 2):
            #POR ID
            nKNN = 10
            toSearch = searchById(lista_vectores, diccionario_ids_name)
            similar = tree.KNN(toSearch,nKNN)

        else:
            #POR GRUPO DE CARACTERISTICAS
            nKNN = 10
            toSearch = searchGroupByCart()
        
        similar = tree.KNN(toSearch,nKNN)     
        printSimilars()