import pytest

from analysis.analyzer import Analyzer


def test_nao_deve_instanciar_analyzer():

    with pytest.raises(TypeError):

        Analyzer()