# entidades/conteudo.py

from typing import TYPE_CHECKING

# Adicionando para evitar problema de importação circular
if TYPE_CHECKING:
    from .interacao import Interacao

# Define a classe base Conteudo e suas funcionalidades de engajamento e consumo
class Conteudo:
    # Construtor
    def __init__(self, id_conteudo: int, nome_conteudo: str) -> None:
        # Identificador do conteúdo
        self._id_conteudo = id_conteudo
        # Nome ou título do conteúdo
        self._nome_conteudo = nome_conteudo
        # Lista para armazenar interações (ex.: play, like, comentário)
        self._interacoes = []  # lista de objetos Interacao

    # Getters e Setters
    @property
    def id_conteudo(self) -> int:
        return self._id_conteudo

    @id_conteudo.setter
    def id_conteudo(self, id: int) -> None:
        self._id_conteudo = id

    @property
    def nome_conteudo(self) -> str:
        return self._nome_conteudo

    @nome_conteudo.setter
    def nome_conteudo(self, nome: str) -> None:
        self._nome_conteudo = nome

    @property
    def interacoes(self):
        # Retorna a lista de interações
        return self._interacoes

    # Métodos de interação
    def adicionar_interacao(self, interacao: 'Interacao') -> None:
        """Adiciona uma nova interação ao conteúdo."""
        self._interacoes.append(interacao)

    def calcular_total_interacoes_engajamento(self) -> int:
        """Retorna o total de interações registradas."""
        return len(self._interacoes)

    def calcular_contagem_por_tipo_interacao(self) -> dict:
        """Retorna um dicionário mapeando cada tipo de interação à sua contagem."""
        contagem = {}
        for inter in self._interacoes:
            tipo = getattr(inter, 'tipo', None)
            if tipo is None:
                continue
            contagem[tipo] = contagem.get(tipo, 0) + 1
        return contagem

    def calcular_tempo_total_consumo(self) -> int:
        """Soma o tempo consumido (em segundos) de todas as interações que tenham esse atributo."""
        total = 0
        for inter in self._interacoes:
            tempo = getattr(inter, 'tempo_consumo_seg', 0)
            if isinstance(tempo, (int, float)):
                total += tempo
        return total

    def calcular_media_tempo_consumo(self) -> float:
        """Calcula a média de tempo consumido entre as interações que possuam tempo de consumo."""
        tempos = []
        for inter in self._interacoes:
            tempo = getattr(inter, 'tempo_consumo_seg', 0)
            if tempo > 0:
                tempos.append(tempo)
        if not tempos:
            return 0.0
        return sum(tempos) / len(tempos)

    def listar_comentarios(self) -> list:
        """Retorna lista com os textos de comentários de todas as interações do tipo comentário."""
        comentarios = []
        for inter in self._interacoes:
            if getattr(inter, 'tipo', None) == 'comentario':
                texto = getattr(inter, 'comentario', None)
                if texto:
                    comentarios.append(texto)
        return comentarios

    # Métodos mágicos para representação
    def __str__(self) -> str:
        relatorio = f"ID: {self.id_conteudo}\n"
        relatorio += f"Conteúdo: {self.nome_conteudo}\n"
        relatorio += "\n===============================\n"
        return relatorio

    def __repr__(self) -> str:
        return f"Conteudo(id_conteudo={self.id_conteudo}, nome_conteudo={self.nome_conteudo})"


# Subclasses (Herança e Polimorfismo)

# Subclasse para vídeos: armazena duração total e calcula % médio assistido
class Video(Conteudo):
    def __init__(self, id_conteudo: int, nome_conteudo: str, duracao_total_video_seg: int) -> None:
        # Chama o construtor da classe base
        super().__init__(id_conteudo, nome_conteudo)
        # Duração total do vídeo em segundos
        self.__duracao_total_video_seg = duracao_total_video_seg

    @property
    def duracao_total_video_seg(self) -> int:
        return self.__duracao_total_video_seg

    def calcular_percentual_medio_assistido(self) -> float:
        """Calcula (tempo médio consumido / duração total) * 100."""
        if self.__duracao_total_video_seg <= 0:
            return 0.0
        tempo_medio = self.calcular_media_tempo_consumo()
        return (tempo_medio / self.__duracao_total_video_seg) * 100


# Subclasse para podcasts: armazena duração total dos episódios e calcula % médio assistido
class Podcast(Conteudo):
    def __init__(self, id_conteudo: int, nome_conteudo: str, duracao_total_episodio_seg: int = 0) -> None:
        # Construtor base
        super().__init__(id_conteudo, nome_conteudo)
        # Duração total do episódio em segundos (opcional)
        self.__duracao_total_episodio_seg = duracao_total_episodio_seg

    @property
    def duracao_total_episodio_seg(self) -> int:
        return self.__duracao_total_episodio_seg

    def calcular_percentual_medio_assistido(self) -> float:
        """Calcula (tempo médio consumido / duração total do episódio) * 100."""
        if self.__duracao_total_episodio_seg <= 0:
            return 0.0
        tempo_medio = self.calcular_media_tempo_consumo()
        return (tempo_medio / self.__duracao_total_episodio_seg) * 100


# Subclasse para artigos: armazena tempo de leitura estimado e calcula % médio lido
class Artigo(Conteudo):
    def __init__(self, id_conteudo: int, nome_conteudo: str, tempo_leitura_estimado_seg: int) -> None:
        # Construtor base
        super().__init__(id_conteudo, nome_conteudo)
        # Tempo de leitura estimado em segundos
        self.__tempo_leitura_estimado_seg = tempo_leitura_estimado_seg

    @property
    def tempo_leitura_estimado_seg(self) -> int:
        return self.__tempo_leitura_estimado_seg

    def calcular_percentual_medio_assistido(self) -> float:
        """Calcula (tempo médio lido / tempo de leitura estimado) * 100."""
        if self.__tempo_leitura_estimado_seg <= 0:
            return 0.0
        tempo_medio = self.calcular_media_tempo_consumo()
        return (tempo_medio / self.__tempo_leitura_estimado_seg) * 100
