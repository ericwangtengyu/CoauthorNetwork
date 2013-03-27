'''
Created on Mar 25, 2013

@author: Tengyu
'''
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import Graph

if __name__ == '__main__':
    pass

def degreeAnalysis(G):
    '''
    Analyze the degree distribution
    '''
    tempY=nx.degree_histogram(G)
    tempX=list(range(0,len(tempY)+1)) # isolated node's degree = 0
    X=[];Y=[]
    for i in range(1,len(tempY)):# here I discard all isolated nodes.
        if tempY[i]!=0:
            Y.append(np.log(tempY[i]))
            X.append(np.log(tempX[i]))
    plt.plot(X,Y,'o')
    plt.xlabel('log(k)')
    plt.ylabel('logN(k)')
    plt.title('Node degree analysis')
    plt.show()       
            
def componentAnalysis(G):
    '''
    Analyze the connected component, question 1)
    '''
    pass

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

