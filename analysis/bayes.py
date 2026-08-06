from analysis.bayes_evidence import BayesEvidence

class Bayes:

    def posterior(
        self,
        priori: float,
        evidencias: list[BayesEvidence]
    ) -> float:

        posterior = priori

        for evidencia in evidencias:
            posterior *= evidencia.likelihood

        return posterior