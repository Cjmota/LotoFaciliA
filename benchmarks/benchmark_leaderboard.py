from dataclasses import dataclass

from benchmarks.benchmark_ranking import BenchmarkRanking


@dataclass(slots=True)
class BenchmarkLeaderboard:

    rankings: dict[str, BenchmarkRanking]
    
    @property
    def metricas(self) -> tuple[str, ...]:

        return tuple(self.rankings.keys())

    def obter(
        self,
        metrica: str
    ) -> BenchmarkRanking:

        return self.rankings[metrica]
    
    def __getitem__(
        self,
        metrica: str
    ) -> BenchmarkRanking:

        return self.rankings[metrica]

    def __contains__(
        self,
        metrica: str
    ) -> bool:

        return metrica in self.rankings
    
    def __iter__(self):

        return iter(self.rankings.items())
    
    def __len__(self):

        return len(self.rankings)
    
   