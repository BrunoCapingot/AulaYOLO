import os

class Arquivo:
    def __init__(self, nome = None, local_origem = None, nome_destino = None, local_destino = None, classe = None, subclasse = None):
        self.nome = nome
        self.classe = classe
        self.subclasse = subclasse
        self.local_origem: str = local_origem
        self.local_destino: str = local_destino
        self.nome_destino: str = nome_destino

