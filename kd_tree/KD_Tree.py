from typing import List

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
        self.correlative = correlative
        # Dimension en la que trabaja
        self.dim = len(self.vector)

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
            self.root = KD_Node(vector, correlative)
            return self.root
            