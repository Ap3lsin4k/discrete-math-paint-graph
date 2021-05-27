class Vertex:
    id: int
    color: str

    def __init__(self, id):
        self.id = id
        self.color = None

    def __eq__(self, other):
        return self.id == other.id and self.color == self.color

    def __hash__(self):
        return hash(repr(self))

    def __repr__(self):
        return "Vertex #" + str(self.id)
