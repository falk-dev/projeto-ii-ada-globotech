"""
Atributos: __id_conteudo, __nome_conteudo, __interacoes (lista de objetos Interacao).

Métodos:

adicionar_interacao(), calcular_total_interacoes_engajamento().

calcular_tempo_total_consumo(), listar_comentarios(), etc.

Subclasses de Conteudo (Herança/Polimorfismo):

Video: Método calcular_percentual_medio_assistido().

Podcast e Artigo: Atributos específicos de duração.

"""


class Conteudo:
    # Construtor
    def __init__(self, id_conteudo: int, nome_conteudo: str) -> None:
        self._id_conteudo: int = id_conteudo
        self._nome_conteudo: str = nome_conteudo
        self._interacoes: list = []

    # Getters e Setters
    @property
    def id_conteudo(self) -> int:
        return self._id_conteudo

    @id_conteudo.setter
    def id_conteudo(self, id: int) -> int:
        self._id_conteudo = id

    @property
    def nome_conteudo(self) -> str:
        return self._nome_conteudo

    @id_conteudo.setter
    def nome_conteudo(self, nome: str) -> str:
        self._nome_conteudo = nome

    # Métodos
    def adicionar_interacao(self, interacao): 
        pass

    def calcular_total_interacoes_engajamento(self):
        pass

    def calcular_contagem_por_tipo_interacao(self):
        pass

    def calcular_tempo_total_consumo(self):
        pass

    def calcular_media_tempo_consumo(self):
        pass

    def listar_comentarios(self):
        pass

    # Métodos mágicos
    def __str__(self):
        pass

    def __repr__(self):
        return f"Curso(id_conteudo={self._id_conteudo}, nome_conteudo={self._nome_conteudo})"


class Video(Conteudo):
    pass

class Podcast(Conteudo):
    pass

class Artigo(Conteudo):
    pass


