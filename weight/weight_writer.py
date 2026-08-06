import json

class WeightWriter:
    
    def __init__(
        self,
        arquivo="pesos_estatisticos.json"
    ):
        self.arquivo = arquivo

    def salvar(

        self,

        pesos
    ):
        
        dados = {}
        
        for categoria, valores in pesos.items():
            
            dados[categoria] = {}
            
            for valor, peso in valores.items():

                dados[categoria][
                    self.normalizar_chave(valor)
                ] = peso.to_dict()
                
        with open(
            
            self.arquivo,
            
            "w",
            
            encoding="utf8"
        
        ) as f:
            
            json.dump(
                
                dados,
                
                f,

                indent=4,

                ensure_ascii=False

            )
        
    
    @staticmethod
    def normalizar_chave(valor):

        if isinstance(valor, float) and valor.is_integer():
            return str(int(valor))

        return str(valor)