from analysis.feature_metadata import FeatureMetadata


def test_deve_conter_chaves_de_probabilidade():

    assert FeatureMetadata.PROB_SOMA == "prob_soma"
    assert FeatureMetadata.PROB_PARES == "prob_pares"
    assert FeatureMetadata.PROB_IMPARES == "prob_impares"
    assert FeatureMetadata.PROB_CONSECUTIVOS == "prob_consecutivos"
    assert FeatureMetadata.PROB_LINHAS == "prob_linhas"
    assert FeatureMetadata.PROB_COLUNAS == "prob_colunas"

def test_deve_conter_chaves_dos_demais_resultados():

    assert FeatureMetadata.ZSCORE_SOMA == "zscore_soma"
    assert FeatureMetadata.ZSCORE_PARES == "zscore_pares"
    assert FeatureMetadata.ZSCORE_IMPARES == "zscore_impares"
    assert FeatureMetadata.ZSCORE_CONSECUTIVOS == "zscore_consecutivos"

    assert FeatureMetadata.MARKOV_SOMA == "markov_soma"

    assert FeatureMetadata.BAYES == "bayes"

    assert FeatureMetadata.SCORE == "score"

