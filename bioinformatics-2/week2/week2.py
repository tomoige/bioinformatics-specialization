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
    if not first and (start_node == current_node):
        return accum, adjacency_list
    rand_index = random.randint(0,len(options) - 1)
    next_node = options[rand_index]
    adjacency_list[current_node].pop(rand_index)
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
        eulerian_cycle = update_full_path(eulerian_cycle, new_start, cycle)
        empty = check_adj_list_empty(adjacency_list)

    return eulerian_cycle

print(get_eulerian_cycle(adjacency_list, 6))

# with open("week2-1.txt") as f:
#     lines = f.read().strip().splitlines()
#     adjacency_list = {}
#     for line in lines:
#         splitlines = line.split(":")
#         key = int(splitlines[0])
#         value = list(map(int, splitlines[1][1:].split(" ")))
#         adjacency_list[key] = value
#     print("answer: ")
#     res = get_eulerian_cycle(adjacency_list, 1)
#     res_string = ""
#     for item in res:
#         res_string += str(item) + " "
#     print(res_string)
#     with open("week2-1-answer.txt", "x") as f2:
#         f2.write(res_string)

def find_end(adjacency_list):
    nodes_with_next = []
    for (key, value) in adjacency_list.items():
        nodes_with_next.append(key)
    for i in adjacency_list:
        for j in adjacency_list[i]:
            if j not in nodes_with_next:
                return j

sample_list = {
    0: [2],
    1: [3],
    2: [1],
    3: [0, 4],
    6: [3, 7],
    7: [8],
    8: [9],
    9: [6]
}

print(find_end(sample_list))

def work_back(current, adjacency_list, accum):
    accum.insert(0, current)
    empty = check_adj_list_empty(adjacency_list)
    if empty:
        return accum
    for key, value in adjacency_list.items():
        for node in value:
            if node == current:
                new_adj = adjacency_list
                new_adj[key].remove(current)
                return work_back(key, new_adj, accum)

print("returning: ", work_back(4, sample_list, []))

with open("week2-2.txt") as f:
    lines = f.read().strip().splitlines()
    adj_list = {}
    for line in lines:
        split_line = line.split(": ")
        adj_list[int(split_line[0])] = list(map(int, split_line[1].split(" ")))
    print(adj_list)
    end = find_end(adj_list)
    print(end)
    res = work_back(end, adj_list, [])
    print(res)

# def get_eulerian_path(adjacency_list)
