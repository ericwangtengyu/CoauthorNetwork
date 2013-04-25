'''
Created on Mar 25, 2013

@author: Tengyu
@author: Chutian Charlie
'''
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import Graph
from random import randint

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
    
def nodeDistance(G, rootNode,targetNode):
    '''
    This function is for question 3)-Charlie
    Get the distance k between root and target node
    '''        
    k=nx.shortest_path_length(G, rootNode,targetNode)           
    return k

def nodeDistanceAnalysis(G):
    '''
    Analyze the node distance and solve question 3) and 4)
    '''
    H=nx.connected_component_subgraphs(G)
    rootNode=randint(0,H[0].number_of_nodes())# select a root from giant component

    r=[0 for k in range(H[0].number_of_nodes())]#list for r(k) 
    
    for targetNode in range(H[0].number_of_nodes()):
        distance=nodeDistance(G, H[0].nodes()[rootNode],H[0].nodes()[targetNode])          
        r[distance]=r[distance]+1   # compute r(k) where k is the distance between root with current node

    
    for findMax in range(H[0].number_of_nodes()):# output Kmax
        
        if r[findMax]==0:
            MaxK=findMax
            print(MaxK)
            break
        
    rk=[0 for k in range(MaxK)]#re store r values in rk[]
    sum=0    # for computing average distance
    for k in range(MaxK):
        rk[k]=r[k]
        sum=sum+r[k]*k
    
    averageRk=sum/H[0].number_of_nodes()
    print(averageRk)
    print(rk)
    k=range(MaxK)    
    plt.bar(k,rk)    #plot bar chart 
    plt.show()
    
G=Graph.Graph()
G.buildGraph('inputFile/papers.lst')
#degreeAnalysis(G.graph)
#componentAnalysis(G.graph)
nodeDistanceAnalysis(G.graph)