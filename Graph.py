
'''
Demonstration of some simple graph algorithms.
    
@author: Jingsai Liang

Augustine Valdez
Sept 18, 19
'''

import sys

class GraphAlgorithms:
    
    '''
    Reads in the specified input file containing
    adjacent edges in a graph and constructs an
    adjacency list.

    The adjacency list is a dictionary that maps
    a vertex to its adjacent vertices.
    '''
    def __init__(self, fileName): 
    
        graphFile = open(fileName)

        '''
        create an initially empty dictionary representing
        an adjacency list of the graph
        '''
        self.adjacencyList = { }
    
        '''
        collection of vertices in the graph (there may be duplicates)
        '''
        self.vertices = [ ]

        for line in graphFile:
            '''
            Get the two vertices
        
            Python lets us assign two variables with one
            assignment statement.
            '''
            (firstVertex, secondVertex) = line.split()
        
            '''
            Add the two vertices to the list of vertices
            At this point, duplicates are ok as later
            operations will retrieve the set of vertices.
            '''
            self.vertices.append(firstVertex)
            self.vertices.append(secondVertex)

            '''
            Check if the first vertex is in the adjacency list.
            If not, add it to the adjacency list.
            '''
            if firstVertex not in self.adjacencyList:
                self.adjacencyList[firstVertex] = [ ]

            '''
            Add the second vertex to the adjacency list of the first vertex.
            '''
            self.adjacencyList[firstVertex].append(secondVertex)
        
        # creates and sort a set of vertices (removes duplicates)
        self.vertices = list(set(self.vertices))
        self.vertices.sort()

        # sort adjacency list for each vertex
        for vertex in self.adjacencyList:
            self.adjacencyList[vertex].sort()

    '''
    Begins the DFS algorithm.
    '''
    def DFSInit(self):
        # initially all vertices are considered unknown
        self.unVisitedVertices = list(set(self.vertices))
        # initialize path as an empty string
        self.path = ""

    '''
    depth-first traversal of specified graph
    '''
    def DFS(self, method):
        self.DFSInit()
        if method is 'recursive':
            #your code
            for v in self.vertices:
                if v in self.unVisitedVertices:
                    self.DFS_recur(v)
            return self.path
            
        elif method is 'stack':
            for v in self.vertices:
                if v in self.unVisitedVertices:
                    self.DFS_stack(v)

            return self.path
            

    def DFS_recur(self,vertex):
        # Your code goes here:+
        self.path += self.unVisitedVertices.pop(self.unVisitedVertices.index(vertex))
        for v in self.adjacencyList[vertex]:
            if v in self.unVisitedVertices:
                self.DFS_recur(v)
        
     
    def DFS_stack(self, vertex):
        # Your code goes here:
        stack = []
        stack.append(vertex)
        while stack:
            vertex = stack.pop()
            if vertex in self.unVisitedVertices:
                self.path += self.unVisitedVertices.pop(self.unVisitedVertices.index(vertex))
                for w in self.adjacencyList[vertex]:
                    if w in self.unVisitedVertices:
                        stack.append(w)

    def BFSInit(self):
        # initially all vertices are considered unknown
        self.unVisitedVertices = list(set(self.vertices))
        # initialize path as an empty string
        self.path = ""
        
    def BFS(self):
        self.BFSInit()
        queue = []
        # Your code goes here:
        for v in self.vertices:
            if v in self.unVisitedVertices:
                self.BFS_queue(v)
        return self.path

    def BFS_queue(self, v):
        queue = []
        # Your code goes here:
        self.path += self.unVisitedVertices.pop(self.unVisitedVertices.index(v))
        queue.insert(0,v)
        while queue:
            queue.pop()
            for w in self.adjacencyList[v]:
                if w in self.unVisitedVertices:
                    self.path += self.unVisitedVertices.pop(self.unVisitedVertices.index(w))
                    queue.insert(0,w)
        return self.path

    def hasCycle(self):
        for v in self.vertices:
            if v not in self.unVisitedVertices:
                return True          

    # Work on this function for at most 10 extra points
    def shortestpath(self, p, q):
        # Your code goes here:
        pass # delete "pass" after writing your own code here 
  
                
        

        

