import math

def follow_one_best_friend(G, initiators, dict_in):
    in_initiator = {}
    initiators_old = []

    for initiator in initiators:
        if(initiator in dict_in):
            in_initiator[initiator] = dict_in[initiator][:]
    while(initiators_old != initiators):

        initiators_old = initiators[:]

        for u, value in in_initiator.items():
            for v in value:
                if (v not in initiators):
                    weight_v_u = G[v][u]
                    to_add = True
                    for v_neighbor, weight_v_neighbor in enumerate(G[v]):
                        if(weight_v_neighbor != 0):
                            if(u != v_neighbor and weight_v_u < weight_v_neighbor and v_neighbor not in initiators):
                                to_add = False
                    if(to_add):
                        initiators.append(v)
                        if(v in dict_in):
                            in_initiator[v] = dict_in[v][:]
            del in_initiator[u]

    return initiators



def follow_all_best_friend(G, initiators_input, dict_in):

    in_initiator = {}
    initiators_old = []
    initiators = initiators_input

    for initiator in initiators:
        if(initiator in dict_in):
            in_initiator[initiator] = dict_in[initiator][:]
    i = 0
    while(initiators_old != initiators):

        initiators_old = initiators[:]

        for u, value in in_initiator.items():
            for v in value:
                if (v not in initiators):
                    weight_v_u = G[v][u]
                    to_add = True
                    for v_neighbor, weight_v_neighbor in enumerate(G[v]):
                        if(weight_v_neighbor != 0):
                            if(u != v_neighbor and weight_v_u <= weight_v_neighbor and v_neighbor not in initiators):
                                to_add = False

                    if(to_add):
                        initiators.append(v)
                        if(v in dict_in):
                            in_initiator[v] = dict_in[v][:]

            del in_initiator[u]

    return initiators


def follow_best_friend(G, initiators, dict_in, threshold):
    in_initiator = {}
    initiators_old = []

    threshold = str(threshold)
    f, uf = threshold.split('.')
    f = int(f)
    uf = int(uf)

    for initiator in initiators:
        if(initiator in dict_in):
            in_initiator[initiator] = dict_in[initiator][:]

    while(initiators_old != initiators):

        initiators_old = initiators[:]

        for u, value in in_initiator.items():
            for v in value:
                if(v not in initiators):
                    weight_v_u = G[v][u]
                    to_add = True
                    total_neighbor = len(G[v])
                    neighbor_not_cascade = 0
                    max_weight = max(G[v])

                    total_max_neighbor = 0
                    for node, weight_v_node in enumerate(G[v]):
                        if(weight_v_node == max_weight):
                            total_max_neighbor = total_max_neighbor + 1

                    for v_neighbor, weight_v_neighbor in enumerate(G[v]):
                        if(weight_v_neighbor != 0):
                            if(u != v_neighbor and weight_v_neighbor == max_weight and v_neighbor not in initiators):
                                neighbor_not_cascade = neighbor_not_cascade + 1
                    number_float, number_int = math.modf( (float(total_max_neighbor)/uf) * f )
                    if(number_float >= 0.5):
                        number_int = number_int + 1
                    if(neighbor_not_cascade > (total_max_neighbor - number_int )):
                        to_add = False

                    if(to_add):
                        initiators.append(v)
                        if(v in dict_in):
                            in_initiator[v] = dict_in[v][:]

            del in_initiator[u]

    return initiators
