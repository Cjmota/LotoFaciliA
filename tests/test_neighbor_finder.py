
from engine.neighbor_finder import NeighborFinder

def closest(
    self,
    valores,
    alvo
):
    return self.buscar(
        valores,
        alvo
    )

def test_closest():

    finder = NeighborFinder()

    assert finder.closest(
        [4,5,6,7,8,9],
        10
    ) == 9

    assert finder.closest(
        [4,5,6,7,8,9],
        3
    ) == 4

    assert finder.closest(
        [4,5,6,7,8,9],
        7
    ) == 7