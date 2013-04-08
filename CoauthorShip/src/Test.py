'''
Created on Mar 25, 2013

@author: Tengyu
'''
import networkx as nx
import Graph

if __name__ == '__main__':
    pass

def degreeAnalysis(G):
    '''
    Analyze the degree distribution
    '''
    pass

def componentAnalysis(G):
    '''
    Analyze the connected component, question 1)
    '''
    print('--------Connected component analysis--------')
    H=nx.connected_component_subgraphs(G)[0]
    n1=H.number_of_nodes()
    n=G.number_of_nodes()
    print('Number of Nodes in the largest component: ',n1)
    print('Number of Nodes in total: ',n)
    print('The ratio is: ',float(n1)/n)
    
def nodeDistance(G, root, k):
    '''
    Get the number of nodes at distance exactly k from the root, qusetion 2)
    '''
    pass

def nodeDiatanceAnalysis(G):
    '''
    Analyze the node distance and solve question 3) and 4)
    '''
    pass

G=Graph.Graph()
G.buildGraph('inputFile/papers.lst')
componentAnalysis(G.graph)


