def legacy_paint(nx_graph, edges_list, nodes):
    colors = ["red", "blue", "green", "orange", "yellow", "violet", "gray", "brown"]
    nx_graph.add_edges_from(edges_list, color='b')
    val_map = {}
    val_map.update({nodes[0]: "red"})
    for node in nodes:
        i = 0
        for edge in edges_list:
            if node in edge:
                i += 1
        while node not in val_map:
            for j in range(i):
                color = 0
                for edge in edges_list:
                    if node in edge:
                        if node == edge[0]:
                            if edge[1] in val_map:
                                while val_map.get(edge[1]) == colors[color]:
                                    color += 1
                        else:
                            if edge[0] in val_map:
                                while val_map.get(edge[0]) == colors[color]:
                                    color += 1
            val_map.update({node: colors[color]})
    return val_map