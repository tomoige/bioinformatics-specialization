import random

adjacency_list = {
    0: [3],
    1: [0],
    2: [1, 6],
    3: [2],
    4: [2],
    5: [4],
    6: [5, 8],
    7: [9],
    8: [7],
    9: [6],
}



def random_walk(adjacency_list, start_node, current_node, first, accum):
    accum.append(current_node)
    options = adjacency_list[current_node]
    if(len(options) == 0):
        return accum, adjacency_list
    rand_index = random.randint(0,len(options) - 1)
    next_node = options[rand_index]
    adjacency_list[current_node].pop(rand_index)
    if not first and (start_node == current_node):
        print("got to the last place")
        return (accum, adjacency_list)
    else:
        return random_walk(adjacency_list, start_node, next_node, False, accum)

def find_unexplored_in_cycle(adjacency_list, cycle):
    for position in cycle:
        if(len(adjacency_list[position]) > 0):
            return position

(cycle, adj_list) = random_walk(adjacency_list, 0, 0, True, [])
print(cycle, adj_list)
new_start = find_unexplored_in_cycle(adj_list, cycle) # gets a node that has unexplored edges that is in the cycle
(cycle2, adj_list_2) = random_walk(adj_list, new_start, new_start, True, [])
print(cycle2, adj_list_2)

