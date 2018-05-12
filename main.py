from rich_get_richer_model import *
from erdos_renyi import *
from writeMatrixFile import *
from follow_best_friend import *
from math import log10, sqrt
import json
import urllib2

def main(model, cascadeModel, n_nodes, size_iniziators, iterations, p, threshold):

    model_str = ''

    if(model == 1):
        G, dict_in = rich_get_richer_model_graph(n_nodes, p, iterations)
        model_str = 'rich_get_richer_model'
    elif(model == 2):
        G, dict_in = Erdos_Renyi_weight(n_nodes, p)
        model_str = 'erdos_renyi'

    writeMatrixFile("csv/matrix.csv", G)

    initiators_start = []

    if(size_iniziators == 1):
        n_initiators = int(sqrt(n_nodes))

    elif(size_iniziators == 2):
        n_initiators = int(log10(n_nodes))

    elif(size_iniziators == 3):
        n_initiators = int(log10(n_nodes)) * int(sqrt(n_nodes))

    i = 1
    while i <= n_initiators:
        rand = random.randint(0, n_nodes - 1)
        if(rand not in initiators_start):
            initiators_start.append(rand)
            i = i + 1

    initiators_str = str(initiators_start)

    if(cascadeModel == 1):
        end_initiators = follow_one_best_friend(G, initiators_start, dict_in)
        cascadeModel_str = 'follow_one_best_friend'
        threshold_str = '1'
        n_initiators_end = len(end_initiators)

    if(cascadeModel == 2):
        end_initiators = follow_all_best_friend(G, initiators_start, dict_in)
        cascadeModel_str = 'follow_all_best_friend'
        threshold_str = 'all'
        n_initiators_end = len(end_initiators)

    if(cascadeModel == 3):
        end_initiators = follow_best_friend(G, initiators_start, dict_in, threshold)
        cascadeModel_str = 'follow_best_friend'
        threshold_str = str(threshold)
        n_initiators_end = len(end_initiators)

    f = open('csv/Results.csv', "a")

    f.write(model_str + ';' + cascadeModel_str + ';' + threshold_str + ';' + str(n_nodes) + ';' + str(p) + ';' + str(n_initiators) + ';' + str(initiators_str) + ';' + str(n_initiators_end) + ';' + str(end_initiators) + '\n')
