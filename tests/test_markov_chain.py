from analysis.markov_chain import MarkovChain


def test_deve_criar_cadeia():

    chain = MarkovChain()

    assert chain is not None
    
def test_deve_registrar_transicao():

    chain = MarkovChain()

    chain.registrar_transicao("A", "B")

def test_deve_calcular_probabilidade():

    chain = MarkovChain()

    chain.registrar_transicao("A", "B")

    probabilidade = chain.probabilidade("A", "B")

    assert probabilidade == 1.0

def test_deve_prever_proximo_estado():

    chain = MarkovChain()

    chain.registrar_transicao("A", "B")

    proximo_estado = chain.prever_proximo_estado("A")

    assert proximo_estado == "B"

def test_deve_registrar_duas_transicoes():

    chain = MarkovChain()

    chain.registrar_transicao("A", "B")

    chain.registrar_transicao("A", "C")

    assert chain.probabilidade("A", "B") == 0.5

    assert chain.probabilidade("A", "C") == 0.5

def test_deve_prever_estado_mais_frequente():

    chain = MarkovChain()

    chain.registrar_transicao("A", "B")

    chain.registrar_transicao("A", "B")

    chain.registrar_transicao("A", "C")

    assert chain.prever_proximo_estado("A") == "B"
