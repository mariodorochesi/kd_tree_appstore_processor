from typing import List
from utils.utils import distance

class KD_Node:
    '''
        Define un Nodo del KD Tree
    '''
    def __init__(self, vector, id = 0):
        '''
            - Vector representa el vector de Datos del problema.
                Para el caso de la App Store.
                [Tamano , Precio , Rating Usuario , Rating Contenido, Genero]
            
        '''
        #ID del nodo
        self.id = id
        # Nodo Izquierdo
        self.left_node = None
        # Nodo Derecho
        self.right_node = None
        # Vector de Informacion
        self.vector = vector
        # Dimension en la que trabaja
        self.dim = len(self.vector)
        # Elemento verificador del nodo
        self.deep = 0
        
    def __str__(self):
        return str(self.vector)


class KD_Tree:
    '''
        Define la estructura del KD Tree
    '''
    def __init__(self, root : KD_Node =None):
        self.root = root

    
    
    #Funcion para generar el arbol de manera iterativa (agregando nodo x nodo)
    def buildTree(self, NewNode, Node=None):
        if(Node is None):
            Node = self.root

        #profundidad de la comparación
        index = (Node.deep)%(Node.dim)
        NewNode.deep = Node.deep+1 

        #Se agrega un nodo a la derecha
        if(Node.vector[index] > NewNode.vector[index]):
            if Node.left_node is None:
                Node.left_node = NewNode
            else:
                self.buildTree(NewNode,Node.left_node )
                return NewNode.deep
        else:
            if Node.right_node is None:
                Node.right_node = NewNode
            else:
                self.buildTree(NewNode, Node.right_node)         
                return NewNode.deep    
    


    def KNN(self, node, n):
        N = []
        S = []
        S.append(self.root)
        max_val = 1000000000000000000

        while(len(S) > 0):
            n_actual = S.pop()

            #Distancia entre el nodo actual del arbol y el nodo que se desea buscar
            d = distance(node.vector,n_actual.vector)
            
            #Se agrega el nodo al vecindario
            if(len(N) < n):
                N.append(n_actual)
            else: 
                if(d > 0.0 and d < max_val):
                    N.pop()
                    N.append(n_actual)
                    N = sorted(N, key = lambda x: distance(x.vector,node.vector) )
            
                    #Se busca el actual mayor
                aux_max = 0 
                    
                for i in N:
                    if distance(i.vector, n_actual.vector) > aux_max:
                        aux_max = distance(i.vector, n_actual.vector)
                max_val = aux_max

            #Se agregan nuevos hijos
            if(n_actual.right_node is not None):
                S.append(n_actual.right_node)
            if(n_actual.left_node is not None):
                S.append(n_actual.left_node)
        return N
    
    
    def printTree(self,node=None):
        if(node is None):
            print("ROOT: "+str(self.root.id))
            print(self.root.vector)

            if(self.root.left_node is not None):
                print("FROM " + str(self.root.id) + " LEFT SON " + str(self.root.left_node.id))
                print(self.root.left_node.vector)
                self.printTree(self.root.left_node)
            
            if(self.root.right_node is not None):
                print("FROM " + str(self.root.id) +" RIGHT SON "+str(self.root.right_node.id))
                print(self.root.right_node)    
                
            if(self.root.left_node is not None):
                self.printTree(self.root.left_node)
            
            if(self.root.right_node is not None):
                self.printTree(self.root.right_node)

        else:
            if(node.left_node is not None):
                print("FROM " + str(node.id) +" LEFT SON "+ str(node.left_node.id))
                print(node.left_node.vector)
                
            if(node.right_node is not None):
                print("FROM " + str(node.id) +" RIGHT SON "+str(node.right_node.id))
                print(node.right_node.vector)
                
            if(node.left_node is not None):
                self.printTree(node.left_node)
            
            if(node.right_node is not None):
                self.printTree(node.right_node)
            