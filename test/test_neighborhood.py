from main import get_2nd_neighbourhood
from conftest import *


def get_variant(nzk: int):
    nzk = nzk % 6 + 1
    return nzk


def test_nothing():
    assert get_variant(nzk=423) == 3 + 1
    assert get_variant(nzk=411) == 3 + 1


@pytest.mark.skip("Don't need neighbourhood of first order yet")
def test_neighbourhood_of_first_order(my_stupid_graph):
    view_vertex = Vertex(0)
    res = get_2nd_neighbourhood(1, my_stupid_graph, view_vertex)
    assert len(res) == 1
    assert res == [Vertex(1)]
    assert Vertex(1) in res


def test_neighborhood_of_second_order(my_stupid_graph):
    view_vertex = Vertex(0)
    res= get_2nd_neighbourhood(my_stupid_graph, view_vertex)

    assert Vertex(2) in res
    assert len(res) == 1


def test_neighborhood_of_second_order2(my_stupid_graph):
    complex_graph = [set(), {Vertex(2), Vertex(4)}, {Vertex(1), Vertex(3)}, {Vertex(2)}, {Vertex(1), Vertex(5)}, {Vertex(4)}]
    view_vertex = Vertex(1)
    res = get_2nd_neighbourhood(complex_graph, Vertex(1))
    assert Vertex(3) in res
    assert Vertex(5) in res
