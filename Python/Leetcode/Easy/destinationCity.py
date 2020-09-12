"""
You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. 
Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, 
there will be exactly one destination city.

Example 1:

Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo" 
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. 
Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".

Example 2:

Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are: 
"D" -> "B" -> "C" -> "A". 
"B" -> "C" -> "A". 
"C" -> "A". 
"A". 
Clearly the destination city is "A"

"""


def destinationCity(paths):
    start_point = paths[0][0]

    city_graph = {start_point: destination for start_point,
                  destination in paths}

    current_position = start_point
    while current_position in city_graph:
        current_position = city_graph[current_position]
    return current_position


def test():
    path1 = [["London", "New York"], [
        "New York", "Lima"], ["Lima", "Sao Paulo"]]
    path2 = [["B", "C"], ["D", "B"], ["C", "A"]]
    path3 = [["A", "Z"]]
    path4 = [["pYyNGfBYbm", "wxAscRuzOl"], ["kzwEQHfwce", "pYyNGfBYbm"]]

    print("Destination City-->", destinationCity(path1))
    print("Destination City-->", destinationCity(path2))
    print("Destination City-->", destinationCity(path3))
    print("Destination City-->", destinationCity(path4))


test()


# approach 2:

def destinationCity2(paths):

    # for locations in paths:
    #     for cities in locations:

    city_array = [locations for cities in paths for locations in cities]
    destinationCity = city_array[-1]
    return destinationCity


def test2():
    path1 = [["London", "New York"], [
        "New York", "Lima"], ["Lima", "Sao Paulo"]]
    path2 = [["B", "C"], ["D", "B"], ["C", "A"]]
    path3 = [["A", "Z"]]
    path4 = [["pYyNGfBYbm", "wxAscRuzOl"], ["kzwEQHfwce", "pYyNGfBYbm"]]

    print("Destination City[2nd Approach]-->", destinationCity2(path1))
    print("Destination City[2nd Approach]-->", destinationCity2(path2))
    print("Destination City[2nd Approach]-->", destinationCity2(path3))
    print("Destination City[2nd Approach]-->", destinationCity2(path4))


test2()
