"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create a queue to hold vertices to traverse
        vertices_to_visit = Queue()

        # initialize queue with starting vertex
        vertices_to_visit.enqueue(starting_vertex)

        # create a set to keep track of visited vertices
        vertices_already_visited = set()

        while vertices_to_visit.size() > 0:

            # get next vertex in line
            current_vertex = vertices_to_visit.dequeue()

            # process current vertex if it hasn't been visited yet
            if current_vertex not in vertices_already_visited:
                print(current_vertex)

                # mark current vertex as visited
                vertices_already_visited.add(current_vertex)

                # add all neighbors to queue
                for neighbor in self.get_neighbors(current_vertex):
                    vertices_to_visit.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create a stack to hold vertices to traverse
        vertices_to_visit = Stack()

        # initialize stack with starting vertex
        vertices_to_visit.push(starting_vertex)

        # create a set to keep track of visited vertices
        vertices_already_visited = set()

        while vertices_to_visit.size() > 0:

            # get next vertex in line
            current_vertex = vertices_to_visit.pop()

            # process current vertex if it hasn't been visited yet
            if current_vertex not in vertices_already_visited:
                print(current_vertex)

                # mark current vertex as visited
                vertices_already_visited.add(current_vertex)

                # add all neighbors to stack
                for neighbor in self.get_neighbors(current_vertex):
                    vertices_to_visit.push(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        def dft_helper(starting_vertex):

            # process current vertex if it hasn't been visited yet
            if starting_vertex not in vertices_already_visited:
                print(starting_vertex)

                # mark current vertex as visited
                vertices_already_visited.add(starting_vertex)

                # add all neighbors to stack
                for neighbor in self.get_neighbors(starting_vertex):
                    dft_helper(neighbor)
       
        # create a set to keep track of visited vertices
        vertices_already_visited = set()

        dft_helper(starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create a queue to hold vertices to traverse
        vertices_to_visit = Queue()

        # initialize queue with starting vertex
        vertices_to_visit.enqueue(starting_vertex)

        # initialize path so far with starting vertex
        path_so_far = starting_vertex

        # use a dictionary to keep track of visited vertices and their path from the starting node
        vertices_already_visited = dict()

        while vertices_to_visit.size() > 0:

            # get next vertex in line
            current_vertex = vertices_to_visit.dequeue()

            # process current vertex if it hasn't been visited yet
            if current_vertex not in vertices_already_visited:
                print(current_vertex)

                # mark current vertex as visited and store its path at the same time
                vertices_already_visited[current_vertex] = path_so_far + current_vertex
                
                # add all neighbors to queue
                for neighbor in self.get_neighbors(current_vertex):
                    vertices_to_visit.enqueue(neighbor)
            
            # destination vertex found; return its path
            elif current_vertex == destination_vertex:
                return vertices_already_visited[current_vertex]


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("Breadth-first search:", graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("Depth-first search:", graph.dfs(1, 6))
    print("Recursive depth-first search:", graph.dfs_recursive(1, 6))
