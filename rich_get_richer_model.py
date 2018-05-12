import random
from writeMatrixFile import *

def rich_get_richer_model_graph(nodes, p, iterations):

    a = int(p * 100)
    max_weight = 0
    dict_in = {}


    G = [[0 for x in range(nodes)] for y in range(nodes)]

    for j in range(iterations):
        for i in range(nodes):
            r = random.randint(1, 100)
            v = i
            while i == v:
                v = random.randint(0, nodes - 1)

            if(r <= a and i != v):#passo a
                if (G[i][v] == 0):
                    G[i][v] = 1
                    if(v not in dict_in):
                        dict_in[v] = []
                    dict_in[v].append(i)

            elif(i != v):#passo b
                v_neighbors = []

                for h in range(nodes):
                    if (G[v][h] != 0):
                        v_neighbors.append(h)

                if(v_neighbors):
                    v_neighbor_rand = random.choice(v_neighbors)
                    if (G[i][v_neighbor_rand] == 0 and i != v_neighbor_rand):
                        G[i][v_neighbor_rand] = 1 + G[v][v_neighbor_rand]
                        if(v not in dict_in):
                            dict_in[v_neighbor_rand] = []
                        dict_in[v_neighbor_rand].append(i)

                        if (G[i][v_neighbor_rand] > max_weight):
                            max_weight = G[i][v_neighbor_rand]

    for j in range(nodes):
        for i in range(nodes):
            if(G[i][j] != 0):
                G[i][j] = int((max_weight + 1) - int(G[i][j]))

    print('Gafo Creato')
    return G, dict_in
