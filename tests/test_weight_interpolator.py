import pytest

from engine.weight_interpolator import WeightInterpolator
from modelos.weight import Weight

def test_deve_retornar_peso_superior():

    interpolador = WeightInterpolator()

    inferior = Weight(
        probabilidade=10,
        peso_bayes=20,
        percentual=30,
        ranking=1,
        quantidade=100,
        nota=80
    )

    superior = Weight(
        probabilidade=20,
        peso_bayes=40,
        percentual=50,
        ranking=3,
        quantidade=200,
        nota=100
    )

    resultado = interpolador.interpolar(
        valor_inferior=10,
        peso_inferior=inferior,
        valor_superior=20,
        peso_superior=superior,
        valor_procurado=20
    )

    assert resultado == superior