from graphs.graph import Graph


def read_graph_from_file(filename):
    """
    Read in data from the specified filename, and create and return a graph
    object corresponding to that data.

    Arguments:
    filename (string): The relative path of the file to be processed

    Returns:
    Graph: A directed or undirected Graph object containing the specified
    vertices and edges
    """

    # TODO: Use 'open' to open the file

    # TODO: Use the first line (G or D) to determine whether graph is directed 
    # and create a graph object

    # TODO: Use the second line to add the vertices to the graph

    # TODO: Use the 3rd+ line to add the edges to the graph

    graph_obj = None
    with open(filename) as graph_file:
        for index, line in enumerate(graph_file.readlines()):
            line = line.strip()
            if index == 0:
                line_parts = line.split(", ")
                if line_parts[0] not in ("D", "G"):
                    raise(ValueError("Bad graph type"))
                    return
                graph_obj = Graph(
                    is_directed=(line_parts[0] == "D"),
                    lat=float(line_parts[1]),
                    lng=float(line_parts[2])
                )
            elif index == 1:
                for vertex in line.split(';'):
                    vertex_id, sweetness, saltiness, savoriness = vertex.split(", ")
                    if vertex_id == "":
                        continue
                    else:
                        graph_obj.add_vertex(vertex_id, sweetness, saltiness, savoriness)
            else:
                if line == "":
                    continue
                vertices = line[1:-1].split(',')
                graph_obj.add_edge(vertices[0], vertices[1])
    return graph_obj


if __name__ == '__main__':

    graph = read_graph_from_file('test.txt')

    print(graph)