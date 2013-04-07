'''
Created on Mar 25, 2013

@author: Tengyu
'''
import networkx as nx
class Graph:
    '''
    The graph to be built from co-authorship
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.graph=nx.empty_graph()
    
    def buildGraph(self,fileName):
        '''
        Build a graph from input file.
        '''
        line=''
        f = open(fileName,'r')
        while True:
            line=f.readline()[24:]
            if not line:
                break;
            line=line[:line.find(',')]
            if(line==''): #in case there is no author for a paper
                continue
            if line.find(' (') > 0:
                line=line[:line.find(' (')] # remove (Eds.) and (Ed.)
            authors=line.split(' & ')
            count=len(authors)
            if(count==1):
                self.graph.add_node(authors[0]) 
            for i in range(0,count-1):
                for j in range(i+1,count):
                    self.graph.add_edge(authors[i],authors[j])
        return
    
    def getNumNodes(self):
        '''
        Get the number of nodes in the graph
        '''
        return self.graph.number_of_nodes()
    
    def getNumEdges(self):
        '''
        Get the number of edges in the graph
        '''
        return self.graph.number_of_edges()
            
        