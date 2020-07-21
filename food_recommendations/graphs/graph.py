from collections import deque
from operator import itemgetter
 import math
import random

class Vertex(object):
    """
    Defines a single vertex and its neighbors.
    """

    def __init__(self, vertex_id, sweetness=0, saltiness=0, savoriness=0, popularity=1):
        """
        Initialize a vertex and its neighbors dictionary.
        
        Parameters:
        vertex_id (string): A unique identifier to identify this vertex.
        """
        self.__id = vertex_id
        self.__qualities = {
            'sweetness': sweetness,
            'saltiness': saltiness,
            'savoriness': savoriness,
        }
        self.popularity = popularity
        self.__neighbors_dict = {} # id -> object

    def update_qualities(self, quality: str, amount: float):
        self.__qualities[quality] *= amount

    def get_quality(self, quality: str):
        return self.__qualities[quality]

    def add_neighbor(self, vertex_obj):
        """
        Add a neighbor by storing it in the neighbors dictionary.

        Parameters:
        vertex_obj (Vertex): An instance of Vertex to be stored as a neighbor.
        """
        self.__neighbors_dict[vertex_obj.get_id()] = vertex_obj

    def __str__(self):
        """Output the list of neighbors of this vertex."""
        neighbor_ids = list(self.__neighbors_dict.keys())
        return f'{self.__id} adjacent to {neighbor_ids}'

    def __repr__(self):
        """Output the list of neighbors of this vertex."""
        return self.__str__()

    def get_neighbors(self):
        """Return the neighbors of this vertex."""
        return list(self.__neighbors_dict.values())

    def get_id(self):
        """Return the id of this vertex."""
        return self.__id


class Graph:
    """ Graph Class
    Represents a directed or undirected graph.
    """
    def __init__(self, is_directed=True, lat, lng):
        """
        Initialize a graph object with an empty vertex dictionary.

        Parameters:
        is_directed (boolean): Whether the graph is directed (edges go in only one direction).
        """
        self.__vertex_dict = dict() # id -> object
        self.__is_directed = is_directed
        self.__lat = lat
        self.__lng = lng

    def add_vertex(self, vertex_id, sweetness, saltiness, savoriness, num_stars):
        """
        Add a new vertex object to the graph with the given key and return the vertex.
        
        Parameters:
        vertex_id (string): The unique identifier for the new vertex.

        Returns:
        Vertex: The new vertex object.
        """
        new_vertex = Vertex(vertex_id, sweetness, saltiness, savoriness, num_stars)
        self.__vertex_dict[vertex_id] = new_vertex
        return new_vertex
        

   def get_similarity(vertex_1, vertex_2):
       return cosine_similarity(
           [
                vertex_1.get_quality('sweetness'),
                vertex_1.get_quality('saltines'),
                vertex_1.get_quality('savoriness')
           ],
           [
                vertex_2.get_quality('sweetness'),
                vertex_2.get_quality('saltines'),
                vertex_2.get_quality('savoriness')
           ]
        )

    def cosine_similarity(v1,v2):
        # Credit to StackOverflow, since I would normally do this using Numpy
        sumxx, sumxy, sumyy = 0, 0, 0
        for i in range(len(v1)):
            x = v1[i]; y = v2[i]
            sumxx += x*x
            sumyy += y*y
            sumxy += x*y
        return sumxy/math.sqrt(sumxx*sumyy)

    def get_vertex(self, vertex_id) -> Vertex:
        """Return the vertex if it exists."""
        if vertex_id not in self.__vertex_dict:
            return None

        vertex_obj = self.__vertex_dict[vertex_id]
        return vertex_obj

    def add_edge(self, vertex_id1, vertex_id2):
        """
        Add an edge from vertex with id `vertex_id1` to vertex with id `vertex_id2`.

        Parameters:
        vertex_id1 (string): The unique identifier of the first vertex.
        vertex_id2 (string): The unique identifier of the second vertex.
        """
        vertex_1 = self.__vertex_dict[vertex_id1]
        vertex_2 = self.__vertex_dict[vertex_id2]
        vertex_1.add_neighbor(vertex_2)
        if not self.__is_directed:
            vertex_2.add_neighbor(vertex_1)
        
    def get_vertices(self):
        """
        Return all vertices in the graph.
        
        Returns:
        List<Vertex>: The vertex objects contained in the graph.
        """
        return list(self.__vertex_dict.values())

    def contains_id(self, vertex_id):
        return vertex_id in self.__vertex_dict

    def __str__(self):
        """Return a string representation of the graph."""
        return f'Graph with vertices: {self.get_vertices()}'

    def __repr__(self):
        """Return a string representation of the graph."""
        return self.__str__()

    def __get_entry_points__(self, if_not_directed_return_one=True, return_all_values_too=False):
        if not self.__is_directed:
            if if_not_directed_return_one:
                startable_ids = [list(self.__vertex_dict.keys())[0]]
            else:
                startable_ids = list(self.__vertex_dict.keys())
        else:
            startable_ids = set(self.__vertex_dict.keys())
            all_values = set()
            for starting_id in startable_ids:
                neighbors_arr = [neighbor_vertex.get_id() for neighbor_vertex in self.__vertex_dict[starting_id].get_neighbors()]
                all_values.update(neighbors_arr)
            startable_ids = list(startable_ids - all_values)

        return startable_ids if not return_all_values_too else (startable_ids, list(all_values))

    def get_connected_components(self, start_vertex_id=None):
        """
        Return a list of all connected components, with each connected component
        represented as a list of vertex ids.
        """
        # startable_ids, all_values = self.__get_entry_points__(True, True)
        all_values = set(self.__vertex_dict.keys())

        all_seen = {}
        components = {}
        curr_component = -1
        for start_id in all_values:
            if (start_vertex_id is not None and start_vertex_id == start_id) or (start_id in all_seen):
                continue

            curr_component += 1
            temp_component = None
            components[curr_component] = set()
            curr_vertex_obj = self.get_vertex(start_id)
            queue = deque()
            queue.append(curr_vertex_obj)
            while queue:
                current_vertex_obj = queue.pop()
                curr_id = current_vertex_obj.get_id()
                if curr_id in all_seen:
                    correct_component = all_seen[curr_id]
                    if correct_component == curr_component:
                        continue
                    components[correct_component].update(
                        components[curr_component]
                    )
                    components[correct_component].add(curr_id)
                    for id in components[curr_component]:
                        all_seen[id] = correct_component
                    
                    temp_component = curr_component
                    curr_component = correct_component
                    # components.pop(curr_component, None)
                    components[temp_component] = set()
                else:
                    all_seen[curr_id] = curr_component
                    components[curr_component].add(curr_id)
                # Process current node
                # print('Processing neighbors of vertex {}'.format(current_vertex_obj.get_id()))
                # print("Neighbors are", [neighbor.get_id() for neighbor in current_vertex_obj.get_neighbors()])

                # Add its neighbors to the queue
                for neighbor in current_vertex_obj.get_neighbors():
                    queue.append(neighbor)
            curr_component = temp_component - 1 if temp_component else curr_component
            temp_component = None

        return [list(components[component_key]) for component_key in components if len(components[component_key]) > 0]

    


    def sort_by_similarity(self, vertex_id, quality: str =None, weight=1.0, use_popularity=False):
        start_vertex = self.get_vertex(vertex_id)
        if quality is not None:
            start_vertex.update_qualities(quality, weight):

        vertexes = self.get_connected_components(start_vertex_id=vertex_id)
        return sorted(
            vertexes,
            key=vertex: self.get_similarity(start_vertex, vertex) * ( 1.0 if not use_popularity else (
                vertex.popularity
            )
        )


                

