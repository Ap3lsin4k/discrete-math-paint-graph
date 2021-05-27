import copy

from main import fasten_and_remove
from model_entity import Vertex
from painter import paint_two_vertices_with_same_color_and_fasten


def test_controller_three_vertices_two_edges(my_stupid_graph):

    viewpoint = my_stupid_graph[0]

    assert viewpoint[0].color is None
    assert my_stupid_graph[1][0].color is None
    assert my_stupid_graph[2][0].color is None
    assert viewpoint[0].color is not None
    assert my_stupid_graph[1][0].color is not None
    assert my_stupid_graph[2][0].color is not None

    paint_two_vertices_with_same_color_and_fasten(my_stupid_graph, viewpoint)

    assert viewpoint[0].color == my_stupid_graph[2][0].color
    assert my_stupid_graph[0][0].color == my_stupid_graph[2][0].color


def test_fasten(simplified_graph):
    second_neighbor_vertex = Vertex(5)

    adjacent_to_second_neighbor = simplified_graph[second_neighbor_vertex.id]
    fasten_and_remove(simplified_graph, Vertex(1))
    adjacent_to_start_point = copy.deepcopy(simplified_graph[1])
    for adj in adjacent_to_second_neighbor:
        # fasten to first viewpoint

        assert adj in adjacent_to_start_point

    assert len(simplified_graph[second_nceighbor_vertex.id]) == 0
