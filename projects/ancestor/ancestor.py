def earliest_ancestor(test_ancestors, starting_vertex):
    adjacency_list = list(test_ancestors)
    visited = set()
    stack = []
    stack.append([starting_vertex])
    possible_paths = []
    while len(stack) > 0:
        path = stack.pop()
        vertex = path[-1]
        if vertex not in visited:
            visited.add(vertex)
            if vertex in adjacency_list:
                for neighbor in adjacency_list[vertex]:
                    if neighbor == None:
                        pass
                    else:
                        path_copy = path.copy()
                        path_copy.append(neighbor)
                        stack.append(path_copy)
            else:
                possible_paths.append(path)
    correct_path = possible_paths[0]
    for path in possible_paths:
        if len(path) > len(correct_path):
            correct_path = path
        elif path[0] < correct_path[0]:
            correct_path = path
    return correct_path



test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

earliest_ancestor(test_ancestors, 6)