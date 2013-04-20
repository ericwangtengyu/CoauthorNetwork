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
    print('--------Node Degree Analysis:--------')
    tempY=nx.degree_histogram(G)
    tempX=list(range(len(tempY))) # isolated node's degree = 0
    X=[];Y=[]
    print('Number of Isolated Node: ',tempY[0])
    for i in range(1,len(tempY)):# here I discard all isolated nodes.
        if tempY[i]!=0:
            Y.append(np.log(tempY[i]))
            X.append(np.log(tempX[i]))
    A=np.array([X,np.ones(len(X))])
    k=np.linalg.lstsq(A.T,Y)[0]
    X=np.array(X)
    regressionLine=k[0]*X+k[1]
    print('Slope of regression line: ',k[0])
    #plt.plot(X,Y,'o',X,regressionLine,label='$Y = %dx$'% k[0])
    plt.plot(X,Y,'o')
    plt.plot(X,regressionLine,'r',label='$Y = %fx+%f$'% (k[0], k[1]))
    plt.legend()
    plt.xlabel('log(k)')
    plt.ylabel('logN(k)')
    plt.title('Node degree analysis')
    plt.show()       
            
def componentAnalysis(G):
    '''
    Analyze the connected component, question 1)
    '''
    print('--------Connected component analysis--------')
    H=nx.connected_component_subgraphs(G)
    n1=H[0].number_of_nodes()
    n=G.number_of_nodes()
    ratio=float(n1)/n
    print('Number of Nodes in the largest component: ',n1)
    print('Number of Nodes in total: ',n)
    print('The ratio is: ',ratio)
    print('The coauthorNetwork has a giant component')
    labels = 'Others','Largest Component'
    fracs = [1-ratio,ratio]
    explode=(0.08, 0)
    plt.title('Connected Component Analysis')
    plt.pie(fracs, explode=explode, labels=labels,autopct='%1.1f%%', shadow=True, startangle=90)
    plt.show()
    
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
degreeAnalysis(G.graph)
componentAnalysis(G.graph)

