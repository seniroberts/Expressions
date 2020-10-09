# Create the Graph Class

from typing import List


class ConnectingCities:
    def __init__(self, city_name: str):
        self.city_name = city_name
        self.all_cities = {}
        self.all_distances = {}

    def get_city_name(self):
        return self.city_name

    def add_next_city(self, city: "ConnectingCities", distance=0):
        self.all_cities[city.get_city_name()] = city
        self. all_distances[city.get_city_name()] = distance

    def __repr__(self):
        return self.city_name
        # return "{}:- {}".format(self.get_city_name(), str(list(self.all_cities.keys())))

    def get_neighbor_cities(self):
        return list(self.all_cities.values())


class AirportGraph:
    def __init__(self, directed=False):
        self.directed = directed
        self.airport_graph = {}

    def create_connecting_city(self, city_name: str):
        if city_name not in self.airport_graph:
            self.airport_graph[city_name] = ConnectingCities(city_name)
        return self.airport_graph[city_name]

    def add_connection_route(self, city1_name: str, city2_name: str, distance=0):
        city1 = self.create_connecting_city(city1_name)
        city2 = self.create_connecting_city(city2_name)
        city1.add_next_city(city2, distance)

        if not self.directed:
            city2.add_next_city(city1, distance)

    def get_city_by_name(self, city_name: str):
        return self.airport_graph[city_name]

    def __repr__(self):
        output_string = ["**** Airport Graph *****\n"]
        for city_name in self.airport_graph:
            output_string.append(str(self.airport_graph[city_name]))
        return "\n".join(output_string)


LAX = AirportGraph()

LAX.add_connection_route("Los-Angeles", "New-York")
LAX.add_connection_route("San-Francisco", "Michigan")
LAX.add_connection_route("New-York", "Houston")
LAX.add_connection_route("Michigan", "Houston")

print(LAX)


def find_path(graph: AirportGraph, from_city: str, destination: str, visited=None):
    from_city_object = graph.get_city_by_name(from_city)
    destination_object = graph.get_city_by_name(destination)
    return dfs(graph, from_city_object, destination_object, visited)


def dfs(graph, from_city, destination, visited):
    if visited is None:
        visited = []

    visited.append(from_city)

    if from_city == destination:
        return visited

    for city in from_city.get_neighbor_cities():
        if city not in visited:
            path = dfs(graph, city, destination, visited)
            if path:
                return path


def BFS(graph, from_city: str, destination: str):
    from_city_object = graph.get_city_by_name(from_city)
    destination_object = graph.get_city_by_name(destination)
    return BFS_helper(graph, from_city_object, destination_object)


def BFS_helper(graph, from_city, destination):
    path = [from_city]
    vertex_and_path = [from_city, path]
    bfs_queue = [vertex_and_path]
    visited = set()
    while bfs_queue:
        current_vertex, path = bfs_queue.pop(0)
        visited.add(current_vertex)

        for neighbor in current_vertex.get_neighbor_cities():
            if neighbor not in visited:
                if neighbor is destination:
                    return path + [neighbor]
                else:
                    bfs_queue.append([neighbor, path + [neighbor]])


def test(input_graph):
    print("*********************************************")
    from_city = "Houston"
    destination = "Los-Angeles"

    print("searching paths from {} ----> {}".format(from_city, destination))
    print("DFS Path ----> ", find_path(input_graph,
                                       from_city, destination))
    print("BFS Path ===>", BFS(input_graph, from_city, destination))

    print("*********************************************")


def pathfinder():
    test(LAX)


pathfinder()
