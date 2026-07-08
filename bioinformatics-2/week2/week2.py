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
    print("hello")
    accum.append(current_node)
    options = adjacency_list[current_node]
    if(len(options) == 0):
        return accum
    rand_index = random.randint(0,len(options) - 1)
    next_node = options[rand_index]
    adjacency_list[current_node].pop(rand_index)
    if not first and (start_node == current_node):
        return accum
    else:
        return random_walk(adjacency_list, start_node, next_node, False, accum)

print(random_walk(adjacency_list, 0, 0, True, []))


