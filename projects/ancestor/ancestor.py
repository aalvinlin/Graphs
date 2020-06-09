from graph import Graph

def earliest_ancestor(ancestors, starting_node):

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
    
    for parent_child_pair in ancestors:
        parent, child = parent_child_pair

        if parent not in known_nodes:
            known_nodes.add(parent)
        
        if child not in known_nodes:
            known_nodes.add(child)

    # add each node to the graph
    for node in known_nodes:
        family_tree.add_vertex(node)

    # add edges to graph. Child nodes point to parent nodes.
    for parent_child_pair in ancestors:
        parent, child = parent_child_pair
        family_tree.add_edge(child, parent)

    print(known_nodes)

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 1))