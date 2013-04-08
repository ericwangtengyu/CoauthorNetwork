'''
Created on Mar 25, 2013

@author: Tengyu
'''
import networkx as nx
import matplotlib.pyplot as plt
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


