import igraph
import random


def Erdos_Renyi_weight(nodes, p):

    a = int(p * 100)
    dict_in = {}

    G = [[0 for x in range(nodes)] for y in range(nodes)]
    mylist = []
    mylist = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,1,2,3,4,5,6,1,2,3,4,5,1,2,3,4,1,2,3,1,2,1]
    for i in range(len(G)):
        for j in range(len(G[0])):
            r = random.randint(1, 100)
            if(r <= a):
                if(i != j):
                    G[i][j] = random.choice(mylist)
                    if(j not in dict_in):
                        dict_in[j] = []
                    dict_in[j].append(i)
    print('Gafo Creato')
    return G, dict_in
