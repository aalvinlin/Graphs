from graph import Graph, Queue, Stack

def earliest_ancestor(ancestors, starting_node):
    # return earliest_ancestor_v1(ancestors, starting_node)
    return earliest_ancestor_v2(ancestors, starting_node)

def earliest_ancestor_v1(ancestors, starting_node):

    # # add all ancesters to a dictionary
    # direct_parents = dict()

    # known_parents = set()

    # for parent_child_pair in ancestors:
    #     parent, child = parent_child_pair
    #     direct_parents[child] = parent

    #     # find any parents of starting node
    #     if child == starting_node:
    #         known_parents.add(parent)

    # print("all parents", direct_parents)
    # print("known parents", known_parents)

    # # count generations
    # current_generation = 0

    # create a graph to represent the data
    family_tree = Graph()

    # obtain a list of all nodes used in the graph
    known_nodes = set()
    
    # create a dictionary store paths to each node
    paths_to_ancestors = dict()

    for parent_child_pair in ancestors:
        parent, child = parent_child_pair

        if parent not in known_nodes:
            known_nodes.add(parent)
        
        if child not in known_nodes:
            known_nodes.add(child)

    # add each node to the graph
    # also initialize paths_to_ancestors
    for node in known_nodes:
        family_tree.add_vertex(node)
        paths_to_ancestors[node] = []

    # add edges to graph. Child nodes point to parent nodes.
    for parent_child_pair in ancestors:
        parent, child = parent_child_pair
        family_tree.add_edge(child, parent)

    # create a queue to hold vertices to traverse
    vertices_to_visit = Queue()

    # initialize queue with starting vertex
    vertices_to_visit.enqueue(starting_node)

    while vertices_to_visit.size() > 0:

        # get next vertex in line
        current_vertex = vertices_to_visit.dequeue()

        # find all parents to the starting node
        for parent in family_tree.get_neighbors(current_vertex):

            # update path from child to parent
            copy_of_path_from_child = paths_to_ancestors[current_vertex][:]
            copy_of_path_from_child.append(current_vertex)
            
            # store path in dictionary
            paths_to_ancestors[parent] = copy_of_path_from_child

            # add parent to queue for later processing
            vertices_to_visit.enqueue(parent)

        # no more children: add current vertex to end of path to finish the path
        final_path = paths_to_ancestors[current_vertex][:]
        final_path.append(current_vertex)
        paths_to_ancestors[current_vertex] = final_path

    # search for the longest path
    longest_path = []

    for node in paths_to_ancestors:

        current_path = paths_to_ancestors[node]

        # update longest path if a longer one is found
        if len(current_path) > len(longest_path):
            longest_path = current_path

    # if the length is 1, that means the node has no parents. Return -1.
    if len(longest_path) == 1:
        return -1

    # otherwise, return the last item in the path, which will be the furthest ancestor
    return longest_path[-1]

def earliest_ancestor_v2(ancestors, starting_node):

    known_parents = dict()
    
    depths = dict()

    # store parent-child information immediately available from "ancestors" in a dictionary
    for parent_child_pair in ancestors:
        parent, child = parent_child_pair

        if child not in known_parents:
            known_parents[child] = [parent]
        else:
            known_parents[child].append(parent)

        if parent not in known_parents:
            known_parents[parent] = []

    # assign a generation for each ancestral node that can be reached from a starting node
    def assign_depths(starting_node, current_depth):

        for parent in known_parents[starting_node]:
            
            depths[parent] = current_depth + 1

            assign_depths(parent, current_depth + 1)
    
    assign_depths(starting_node, 0)

    # find the furthest node from the starting node
    deepest_depth = 0
    deepest_node = None

    for node in depths:

        if depths[node] > deepest_depth:
            deepest_depth = depths[node]
            deepest_node = node

    # return -1 if the starting node has no ancestors
    if not deepest_node:
        return -1
    else:
        return deepest_node

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 6))
