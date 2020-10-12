from typing import List
from utils.utils import distance

class KD_Node:
    '''
        Define un Nodo del KD Tree
    '''
    def __init__(self, vector, correlative = None, id = 0):
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
        self.correlative = correlative
        # Dimension en la que trabaja
        self.dim = len(self.vector)
        # Elemento verificador del nodo
        self.deep = 0

        self.id = id

    def __str__(self):
        return str(self.vector)

class KD_Tree:
    '''
        Define la estructura del KD Tree

        AQUI HAY QUE TRABAJAR MUCHO, FALTA CASI TODO POR HACER
    '''
    def __init__(self, root : KD_Node =None):
        self.root = root

    def insert_record(self, vector : List, correlative = None):
        if self.root == None:
            self.root = KD_Node(vector, correlative,0)      
            return self.root
    
    #Funcion para generar el arbol de manera iterativa (agregando nodo x nodo)
    def buildTree(self,Node,NewNode):
        #profundidad de la comparación
        deep = (Node.deep)%(Node.dim)   
        NewNode.deep = (Node.deep+1)%(Node.dim) 
        
        #Se agrega un nodo a la derecha
        if(Node.vector[deep] > NewNode.vector[deep]):
            if Node.left_node is None:
                Node.left_node = NewNode
            else:
                self.buildTree(Node.left_node, NewNode)
                return NewNode.deep
        else:
            if Node.right_node is None:
                Node.right_node = NewNode
            else:
                self.buildTree(Node.right_node, NewNode)         
                return NewNode.deep    
    
    
    def search(self,node):
        actual = self.root
        while(actual is not None):
            if( distance(actual.vector, node.vector) <= 0.00001 ):
                print("NO HAY NAPO")
                return actual
            elif( distance(actual.vector, node.vector) > 0.00001 and actual.left_node != None):
                actual = actual.left_node
            elif( distance(actual.vector, node.vector) > 0.00001 and actual.right_node != None):
                actual = actual.right_node
            else: 
                print("NO HAY NAPO") 
                return None
        
    
    def KNN(self, node, n):
        N = []
        S = []
        S.append(self.root)

        while(len(S) > 0):
            n_actual = S.pop()
            
            #Distancia entre el nodo actual del arbol y el nodo que se desea buscar
            d = distance(node.vector,n_actual.vector)
            
            #Se agrega el nodo al vecindario
            if(len(N) < n):
                if(len(N) == 0):
                    N.append(n_actual)
                else:
                    for i in range(len(N)):
                        if( d >= distance( N[i].vector, n_actual.vector) ):
                            N.insert(i,n_actual)
                            break
            else:
                for i in range(n):
                    if(d >= distance( N[i].vector,n_actual.vector )):
                        N.insert(i,n_actual)
                        N.pop()
                        break
            

            #Se agrega el siguiente nodo para visitar
            deep_n = n_actual.deep
            ##print(deep_n)
            
            if n_actual.vector[deep_n] < node.vector[deep_n] :
                if(n_actual.right_node is not None):
                    S.append(n_actual.right_node)
                if(n_actual.left_node is not None):
                    S.append(n_actual.left_node)
            else:
                if(n_actual.left_node is not None):
                    S.append(n_actual.left_node)
                
                if(n_actual.right_node is not None):
                    S.append(n_actual.right_node)
        for x in N:
            print(distance(node.vector, x.vector))

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
            