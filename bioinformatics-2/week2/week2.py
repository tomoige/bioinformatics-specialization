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

# def random_walk(adjacency_list, start_node, current_node, first, accum):
#     accum.append(current_node)
#     options = adjacency_list[current_node]
#     if(len(options) == 0):
#         return accum, adjacency_list
#     if not first and (start_node == current_node):
#         return accum, adjacency_list
#     rand_index = random.randint(0,len(options) - 1)
#     next_node = options[rand_index]
#     adjacency_list[current_node].pop(rand_index)
#     return random_walk(adjacency_list, start_node, next_node, False, accum)

def random_walk(adjacency_list, start_node, first):
    cycle = [start_node]
    current_node = start_node
    options = adjacency_list[current_node]
    current_node = options.pop(0)
    cycle.append(current_node)

    while((current_node != start_node)):
        options = adjacency_list[current_node]
        current_node = options.pop(0)
        cycle.append(current_node)
    
    return cycle, adjacency_list

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
        eulerian_cycle, adjacency_list = random_walk(adjacency_list, start_node, True)
    empty = check_adj_list_empty(adjacency_list)

    while(not empty):
        
        # get next cycle and update adjacency_list
        new_start = find_unexplored_in_cycle(adjacency_list, eulerian_cycle)
        (cycle, adjacency_list) = random_walk(adjacency_list, new_start, True)
        eulerian_cycle = update_full_path(eulerian_cycle, new_start, cycle)
        empty = check_adj_list_empty(adjacency_list)

    return eulerian_cycle

# print(get_eulerian_cycle(adjacency_list, 6))

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

# print(find_end(sample_list))

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

# print("returning: ", work_back(4, sample_list, []))

# with open("week2-2.txt") as f:
#     lines = f.read().strip().splitlines()
#     adj_list = {}
#     for line in lines:
#         split_line = line.split(": ")
#         adj_list[int(split_line[0])] = list(map(int, split_line[1].split(" ")))
#     print(adj_list)
#     end = find_end(adj_list)
#     print(end)
#     res = work_back(end, adj_list, [])
#     print(res)

# count all the in and out degrees of each node
# which has one extra out is the start
# which has one extra in in the end

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

def get_degrees(adjacency_list):
    degree_counts = {}
    for key, value in adjacency_list.items():
        if key not in degree_counts: 
            degree_counts[key] = 0

        degree_counts[key] = degree_counts[key] + len(value)
        for node in value:
            if node not in degree_counts:
                degree_counts[node] = 0
            degree_counts[node] = degree_counts[node] - 1

    return degree_counts

degrees = get_degrees(sample_list)



def get_eulerian_path(adj_list):
    degrees = get_degrees(adj_list)
    start = 0
    end = 0
    for key, value in degrees.items():
        if(value > 0):
            start = key
        if(value < 0):
            end = key
    if end not in adj_list:
        adj_list[end] = [start]
    else:
        adj_list[end].append(start)

    # print(degrees)
    # print(start, end)
    # print(adj_list)

    return get_eulerian_cycle(adj_list, start)[:-1]

# print(get_eulerian_path(sample_list))

# with open("week2-2.txt") as f:
#     lines = f.read().strip().splitlines()
#     adjacency_list = {}
#     for line in lines:
#         splitlines = line.split(":")
#         key = int(splitlines[0])
#         value = list(map(int, splitlines[1][1:].split(" ")))
#         adjacency_list[key] = value
#     print("answer: ")
#     res = get_eulerian_path(adjacency_list)
#     res_string = ""
#     for i in res:
#         res_string += str(i) + " "
#     print(res_string)

def debruijn(patterns):
    graph = {}
    for string in patterns:
        prefix = string[:-1]
        suffix = string[1:]
        if prefix not in graph:
            graph[prefix] = [suffix]
        else:
            graph[prefix].append(suffix)
    return graph

length = 4
patterns = ["CTTA", "ACCA", "TACC", "GGCT", "GCTT", "TTAC"]

def get_conversion(graph):
    conversion = {}
    i = 0
    for key, value in graph.items():
        if key not in conversion:
            conversion[key] = i
            i += 1
        for j in value:
            if j not in conversion:
                conversion[j] = i
                i += 1
    return conversion

def convert(graph, conversion):
    converted_graph = {}
    for key, value in graph.items():
        converted_value = []
        for i in value:
            converted_value.append(conversion[i])
        converted_graph[conversion[key]] = converted_value
    return converted_graph

def reconstruct(path, conversion):
    reverse_conversion = dict((v,k) for k,v in conversion.items())
    string = ""
    for i, node in enumerate(path):
        if i < len(path) - 1:
            string += reverse_conversion[node][0]
        else:
            string += reverse_conversion[node]
    return string

def string_reconstruction(patterns):
    debruijn_graph = debruijn(patterns)
    conversion = get_conversion(debruijn_graph)
    converted_graph = convert(debruijn_graph, conversion)
    res = get_eulerian_path(converted_graph)
    return reconstruct(res, conversion)

print(string_reconstruction(patterns))

with open("week2-3.txt") as f:
    lines = f.read().strip().splitlines()
    patterns = lines[1].split(" ")
    print(string_reconstruction(patterns))

strings = {
    "000",
    "001",
    "010",
    "011",
    "100",
    "101",
    "110",
    "111"
}

print(string_reconstruction(strings))

def generate_binary_strings(k):
    strings = ["0"*k, "0"*(k-1) + "1"]
    stop_str = "1" * k
    for i in range(k-1):
        for j in range(len(strings)):
            addone = strings[j] + "1"
            addzero = strings[j] + "0"
            print(addone[1:])
            print(addzero[1:])     
            strings.append(addone[1:])
            strings.append(addzero[1:])
    ## remove duplicates
    strings_res = []
    for string in strings:
        if string not in strings_res:
            strings_res.append(string)
    return strings_res

strings = generate_binary_strings(8)

print(string_reconstruction(strings))


def get_kmers_from_string(string, k, d=1):
    kmers = []
    for i in range(len(string) - (2*k) - d + 1):
        kmers.append("(" + string[i:i+k] + "|" + string[i+k+d:i+d+2*k] + ")")
    
    return sorted(kmers)

string = "TAATGCCATGGGATGTT"

print(" ".join(get_kmers_from_string(string, 3, 2)))

def prefix(string):
    return string[:-1]

def suffix(string):
    return string[1:]

def create_graph(strings):
    graph = {}
    for string in strings:
        split = string.split("|")
        first_prefix = prefix(split[0])
        second_prefix = prefix(split[1])
        complete_prefix = first_prefix + "|" + second_prefix
        
        first_suffix = suffix(split[0])
        second_suffix = suffix(split[1])
        complete_suffix = first_suffix + "|" + second_suffix

        if complete_prefix not in graph:
            graph[complete_prefix] = [complete_suffix]
        else:
            graph[complete_prefix].append(complete_suffix)
    
    return graph

strings = ["GAGA|TTGA", "TCGT|GATG", "CGTG|ATGT", "TGGT|TGAG", "GTGA|TGTT", "GTGG|GTGA", "TGAG|GTTG", "GGTC|GAGA", "GTCG|AGAT"]


def find_not_empty(matrix):
    for key, value in matrix.items():
        if len(value) > 0:
            return key
    return False

def find_path(matrix):
    path = []
    
    m = matrix
    current_node = find_not_empty(m)
    if not current_node:
        return path, m
    path.append(current_node)
    next_paths = m[current_node]
    while(len(next_paths) > 0):
        next_path = next_paths.pop(0)
        path.append(next_path)
        if(next_path not in m):
            return path, m
        next_paths = m[next_path]
        
    return path, m

paths = []
graph = create_graph(strings)
while(True):
    path, graph = find_path(graph)
    if len(path) == 0:
        break;
    paths.append(path)

def concatenate_paths(paths):
    full_path = paths.pop(0)
    print("full_path is: ", full_path)
    print("first item in full_path is: ", full_path[0])
    for path in paths:
        print("loop full path is: ", full_path)
        first = path[0]
        end = path[-1]
        full_path_first = full_path[0]
        full_path_end = full_path[-1]
        if first == full_path_end:
            full_path.extend(path[1:])
        else:
            path.extend(full_path[1:])
            full_path = path
    return full_path

def create_path(strings):
    paths = []
    graph = create_graph(strings)
    while(True):
        path, graph = find_path(graph)
        if len(path) == 0:
            break;
        paths.append(path)
    concatenated_paths = concatenate_paths(paths)
    ## debug
    # print(paths)
    return concatenated_paths

# print(paths[0])
# concatenated_paths = concatenate_paths(paths)
# print(concatenated_paths)
concatenated_paths = create_path(strings)
print("concatenated paths: ", concatenated_paths)

# GTGG??GTGA
#  TGGT??TGAG
#   GGTC??GAGA
#    GTCG??AGAT
#     TCGT??GATG
#      CGTG??ATGT
#       GTGA??TGTT
#        TGAG??GTTG
#         GAGA??TTGA

sample = [
    "GACC|GCGC", 
    "ACCG|CGCC", 
    "CCGA|GCCG", 
    "CGAG|CCGG",
    "GAGC|CGGA"
]

k = 4
d = 2

def get_patterns(patterns):
    start_parts = []
    end_parts = []
    for string in patterns:
        split = string.split("|")
        start_parts.append(split[0])
        end_parts.append(split[1])
    initial_kmers = []
    terminal_kmers = []
    for i in range(len(start_parts) - 1):
        initial_kmers.append(start_parts[i] + start_parts[i+1][-1])
        terminal_kmers.append(end_parts[i] + end_parts[i+1][-1])
    
    return initial_kmers, terminal_kmers

def string_spelled_by_patterns(patterns):
    string = ""
    for i in range(len(patterns)):
        if i == 0:
            string += patterns[i]
        else:
            string += patterns[i][-1]
    return string

def concatenate_strings(prefixstring, suffixstring, k, d):
    for i in range(k+d+1, len(prefixstring)):
        checking_against = suffixstring[i - k - d]
        if(not (prefixstring[i] == checking_against)):
            print("wrong")
        
    fullstring = prefixstring + suffixstring[len(suffixstring)-(k+d):]
    print("fullstring:", fullstring)
    return fullstring

def string_spelled_by_gapped_patterns(patterns, k, d):
    initial_kmers, terminal_kmers = get_patterns(patterns)
    prefixstring = string_spelled_by_patterns(initial_kmers)
    suffixstring = string_spelled_by_patterns(terminal_kmers)
    concatenated = concatenate_strings(prefixstring, suffixstring, k, d)
    return concatenated

print(string_spelled_by_gapped_patterns(sample, k, d))
    
# with open("week2-4.txt") as f:
#     lines = f.read().strip().splitlines()
#     k, d = list(map(int,lines[0].split(" ")))
#     print(k, d)
#     strings = lines[1].split(" ")
#     print("strings: ", strings)
#     concatenated2 = string_spelled_by_gapped_patterns(strings, k, d)
#     with open("week2-4-answer.txt", "x") as f2:
#         f2.write(concatenated2)

example = [
    "GAGA|TTGA", "TCGT|GATG", "CGTG|ATGT", "TGGT|TGAG", "GTGA|TGTT", "GTGG|GTGA", "TGAG|GTTG", "GGTC|GAGA", "GTCG|AGAT"
]

concatenated_paths = create_path(example)
print(string_spelled_by_gapped_patterns(concatenated_paths, 4, 2))

# with open("week2-5.txt") as f:
#     lines = f.read().strip().splitlines()
#     k, d = list(map(int,lines[0].split(" ")))
#     print(k, d)
#     strings = lines[1].split(" ")
#     print("strings: ", strings)
#     strings2 = create_path(strings)
#     concatenated2 = string_spelled_by_gapped_patterns(strings2, k, d)
#     print(concatenated2)

sample = ["ATG", "ATG", "TGT", "TGG", "CAT", "GGA", "GAT", "AGA"]

graph = debruijn(sample)

# MaximalNonBranchingPaths(Graph)
#     Paths ← empty list
#     for each node v in Graph
#         if v is not a 1-in-1-out node
#             if out(v) > 0
#                 for each outgoing edge (v, w) from v
#                     NonBranchingPath ← the path consisting of single edge (v, w)
#                     while w is a 1-in-1-out node
#                         extend NonBranchingPath by the edge (w, u) 
#                         w ← u
#                     add NonBranchingPath to the set Paths
#     for each isolated cycle Cycle in Graph
#         add Cycle to Paths
#     return Paths
def check_one_in_one_out(node, graph):
    if node not in graph:
        return False
    if (not (len(graph[node]) == 1)):
        return False
    count_in = 0;
    for (key, value) in graph.items():
        for val in value:
            if val == node:
                count_in += 1
    if (not(count_in == 1)):
        return False
    
    return True


def mnbp(graph):
    paths = []
    for (key, value) in graph.items():
        if (not(check_one_in_one_out(key, graph))):
            if len(graph[key]) > 0:
                for out_edge in graph[key]:
                    w = out_edge
                    nbp = [key, out_edge]
                    while check_one_in_one_out(w, graph):
                        u = graph[out_edge][0]
                        nbp.append(u)
                        w = u
                    paths.append(nbp)

    allpathsconcat = []
    for path in paths:
        allpathsconcat.extend(path)
    
    for (key) in graph:
        if(key not in allpathsconcat):
            cycle = [key]
            next_node = graph[key][0]
            while (not(next_node == key)):
                cycle.append(next_node)
                next_node = graph[next_node][0]
            paths.append(cycle)  
            allpathsconcat.extend(cycle) 
    return paths

graph = {
    1: [2],
    2: [3],
    3: [4, 5],
    6: [7],
    7: [6]
}

print(mnbp(graph))

sample = ["ATG", "ATG", "TGT", "TGG", "CAT", "GGA", "GAT", "AGA"]

graph = debruijn(sample)

res = mnbp(graph)
print(res)
contigs = []
for path in res:
    contig = ""
    for i in range(len(path)):
        if i == 0:
            contig += path[i]
        else:
            contig += path[i][-1]
    contigs.append(contig)

print(contigs)

with open("week2-6.txt") as f:
    sample = f.read().strip().split(" ")
    graph = debruijn(sample)
    res = mnbp(graph)
    contigs = []
    for path in res:
        contig = ""
        for i in range(len(path)):
            if i == 0:
                contig += path[i]
            else:
                contig += path[i][-1]
        contigs.append(contig)

    with open("week2-6-answer.txt", "x") as f2:
        f2.write(" ".join(contigs))


