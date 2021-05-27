from model_entity import Vertex


def get_neighbourhood1(o, matrix, vv):
    if o == 1:
        return {matrix[vv.id]}

    res = []
    for vertex_first_order in get_neighbourhood1(1, matrix, vv):
        second_order_vertices = set()
        v1 = vertex_first_order[0]
        second_order_vertices.update(get_neighbourhood1(1, matrix, v1))
        v2 = vertex_first_order[1]
        second_order_vertices.update(get_neighbourhood1(1, matrix, v2))

        second_order_vertices.remove(vv)
        return second_order_vertices


v = Vertex(3)


def get_2nd_neighbourhood(matrix, vv):
    first_order = []
    second_order = []
    for i in matrix[vv.id]:
        first_order.append(i)
    for i in first_order:
        for j in matrix[i.id]:
            second_order.append(j)
    vv.color = 'red'
    second_order[0].color = 'red'
    return second_order

def fasten_and_remove(graph, point):
    second_order = get_2nd_neighbourhood(graph, point)
    second_neighbor = second_order[0]
    fasten(graph, point, second_neighbor)
    graph[second_neighbor.id] = []
    #graph.remove(second_order[3].id)
    # graph.pip(second_order[3].id)
    return graph


def fasten(graph, point, second_neighbor):
    graph[point.id].update(graph[second_neighbor.id])
