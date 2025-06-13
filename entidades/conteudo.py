from typing import TYPE_CHECKING

# Adicionando para evitar problema de importação circular
# Importa apenas quando for chamada, no restante do código não é executado
if TYPE_CHECKING:
    from .interacao import Interacao


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

    @nome_conteudo.setter
    def nome_conteudo(self, nome: str) -> str:
        self._nome_conteudo = nome

    @property
    def interacoes(self):
        return self._interacoes

    # Métodos
    # O tipo 'Interacao' está entre aspas para evitar o problema de importação circular,
    # daí colocando entre aspas, comunica ao Python para "se preocupar" com o tipo apenas quando tudo estiver carregado.
    def adicionar_interacao(self, interacao: "Interacao"):
        self._interacoes.append(interacao)

    def calcular_total_interacoes_engajamento(self):
        pass

    def calcular_contagem_por_tipo_interacao(self):
        pass

    def calcular_tempo_total_consumo(self):
        pass

    def calcular_media_tempo_consumo(self):
        pass

    def listar_comentarios(self) -> list:
        pass

    # Métodos mágicos
    def __str__(self):
        relatorio = f"ID: {self.id_conteudo}\n"
        relatorio += f"Conteúdo: {self.nome_conteudo}\n"
        relatorio += f"\n===============================\n"
        return relatorio

    def __repr__(self):
        return f"Conteudo(id_conteudo={self.id_conteudo}, nome_conteudo={self.nome_conteudo})"


class Video(Conteudo):
    pass


class Podcast(Conteudo):
    pass


class Artigo(Conteudo):
    pass
