from typing import List
from utils.utils import distance
import numpy as np
import copy
import bisect

class KD_Node:
    '''
        Define un Nodo del KD Tree
    '''

    def __init__(self, vector, correlative = None):
        '''
            - Vector representa el vector de Datos del problema.
                Para el caso de la App Store.
                [Tamano , Precio , Rating Usuario , Rating Contenido, Genero]
            - Correlative es una variable utilizada para identificar un vector
            de informacion.
        '''
        # Nodo Izquierdo
        self.left_node = None
        # Nodo Derecho
        self.right_node = None
        # Vector de Informacion
        self.vector = vector
        # Correlativo al Nodo
        self.correlative = list()
        if correlative is not None:
            self.correlative.append(correlative)

    def __str__(self):
        return str(self.vector)

class KD_Tree:
    '''
        Define la estructura del KD Tree

        AQUI HAY QUE TRABAJAR MUCHO, FALTA CASI TODO POR HACER
    '''
    def __init__(self, root : KD_Node =None):
        self.root = root
        self.nodes_dimension = 1
        self.size = 0

    def insert_record(self, root, vector, depth, correlative = None ):
        '''
            root : Nodo desde el cual se compara
            vector : Vector que esta siendo ingresado al arbol
            depth : Profundidad de comparasion del vector
            correlative : Un dato para identificar al nodo

            Esta funcion trabaja de manera recursiva comparando dimensiones 
            y nodos.

        '''

        # Si el nodo de comparacion es vacio
        if root is None:
            # Se crea un nuevo nodo
            root = KD_Node(vector, correlative)
            # Si el arbol se encuentra vacio entonces se agrega a la raiz
            if self.size == 0:
                self.root = root
                self.size +=1
            # Se retorna el nodo creado
            return root

        # Se obtiene la dimension del vector en la cual se va a comparar
        current_dimension = depth % self.nodes_dimension

        # Si la dimension del vector es menor a su padre entonces se coloca a la izquierda
        if vector[current_dimension] < root.vector[current_dimension]:
            root.left_node = self.insert_record(root.left_node, vector,depth +1, correlative)
        # Sino se coloca a la derecha
        else:
            root.right_node = self.insert_record(root.right_node, vector, depth+1, correlative)
        
        # Se retorna el nodo colocado
        return root
        
    def insert(self,vector, correlative = None):
        '''
            Esta funcion utiliza mayoritariamente a la funcion recurisva de arriba
        '''
        if self.size == 0:
            self.nodes_dimension = len(vector)
            return self.insert_record(None, vector, 0, correlative)
        self.size +=1
        return self.insert_record(self.root, vector, 0, correlative)


    def k_nearest(self, cantidad_vecinos, vector, id):
        '''
            1 .- Orden en que se ingresan en la pila. Comparar dimension y decidie
            izquierda o derecha.
            2 .- Verificar si el subarbol puede contener vecinos cercanos. Para eso se
            calcula la distancia en la dimension de corte.
        '''

        if cantidad_vecinos > self.size:
            raise Exception("Se esta solicitando una cantidad mayor a los nodos del arbol")
        
        nodes = list()
        nodes.append(self.root)

        vecinos = list()
        distancia_maxima = 10000

        while len(nodes) != 0:
        
            node = nodes.pop(len(nodes)-1)

            distancia = distance(vector, node.vector)
            if distancia < distancia_maxima and node.correlative[0].id != id:
                if len(vecinos) < cantidad_vecinos:
                    vecinos.append((distancia,node.correlative))
                else:
                    vecinos.pop(-1)
                    vecinos.append((distancia,node.correlative))
                    vecinos = sorted(vecinos, key= lambda x : x[0])
                aux_max = 0
                for i in vecinos:
                    if i[0] > aux_max:
                        aux_max = i[0]
                distancia_maxima = aux_max


            if node.left_node is not None:
                nodes.append(node.left_node)
            if node.right_node is not None:
                nodes.append(node.right_node)

        return vecinos