import pytest
from model_entity import Vertex


@pytest.fixture
def my_stupid_graph():
    model = [None, None, None, None]
    model[0] = [Vertex(1)]
    model[1] = [Vertex(2)]
    model[2] = [Vertex(3)]
    return model

@pytest.fixture
def main_graph():
    graph = [set(), {Vertex(2), Vertex(4)}, {Vertex(3), Vertex(4), Vertex(5), Vertex(6)},
             {Vertex(2), Vertex(6)}, {Vertex(1), Vertex(2), Vertex(5), Vertex(7)}, {Vertex(2), Vertex(4), Vertex(6), Vertex(7),
                                                                                    Vertex(8)},
             {Vertex(2), Vertex(3), Vertex(5), Vertex(8)}, {Vertex(4), Vertex(5), Vertex(8)},
             {Vertex(5), Vertex(6), Vertex(7)}]
    return graph


@pytest.fixture
def simplified_graph():
    graph = [set(), {Vertex(2), Vertex(3), Vertex(4)}, {Vertex(1), Vertex(3), Vertex(4)}, {Vertex(1), Vertex(2), Vertex(4), Vertex(5)},
             {Vertex(1), Vertex(2), Vertex(3)}, {Vertex(3)}]
    return graph