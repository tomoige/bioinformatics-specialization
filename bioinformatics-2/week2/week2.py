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
        return accum, adjacency_list
    else:
        return random_walk(adjacency_list, start_node, next_node, False, accum)

def find_unexplored_in_cycle(adjacency_list, cycle):
    for position in cycle:
        if(len(adjacency_list[position]) > 0):
            return position

def update_full_path(current_path, new_start, new_cycle):
    index = current_path.index(new_start)
    firstHalf = current_path[0:index]
    secondHalf = current_path[index+1:]
    firstHalf.extend(new_cycle)
    firstHalf.extend(secondHalf)
    
    return firstHalf

def check_adj_list_empty(adj_list):
    for (key, value) in adj_list.items():
        if value:
            return False
    return True

def get_eulerian_cycle(adjacency_list, start_node):
    empty = check_adj_list_empty(adjacency_list)
    eulerian_cycle = []

    # initial cycle
    if(not empty):
        eulerian_cycle, adjacency_list = random_walk(adjacency_list, start_node, start_node, True, [])
    empty = check_adj_list_empty(adjacency_list)

    while(not empty):
        
        # get next cycle and update adjacency_list
        new_start = find_unexplored_in_cycle(adjacency_list, eulerian_cycle)
        (cycle, adjacency_list) = random_walk(adjacency_list, new_start, new_start, True, [])
        print("updating: ", eulerian_cycle, " with: ", cycle)
        eulerian_cycle = update_full_path(eulerian_cycle, new_start, cycle)
        empty = check_adj_list_empty(adjacency_list)

    return eulerian_cycle

print(get_eulerian_cycle(adjacency_list, 2))




# (cycle, adj_list) = random_walk(adjacency_list, 0, 0, True, [])
# print(cycle, adj_list)
# print("list status: ", check_adj_list_empty(adj_list))
# new_start = find_unexplored_in_cycle(adj_list, cycle) # gets a node that has unexplored edges that is in the cycle
# (cycle2, adj_list_2) = random_walk(adj_list, new_start, new_start, True, [])
# print(cycle2, adj_list_2)
# print("list status: ", check_adj_list_empty(adj_list))

# print(update_full_path(cycle, new_start, cycle2))


