from typing import TYPE_CHECKING
from collections import Counter


# Adicionando para evitar problema de importação circular
# Daí, para funcionar, precisa que o tipo Interacao seja colocado entre aspas
# Porque informa basicamente: sistema, não se preocupe agora com o tipo desse atributo
# Se preocupe apenas ao finalizar o processamento do programa
if TYPE_CHECKING:
    from .interacao import Interacao


class Conteudo:
    # Construtor
    def __init__(self, id_conteudo: int, nome_conteudo: str) -> None:
        self._id_conteudo: int = id_conteudo
        self._nome_conteudo: str = nome_conteudo
        self._interacoes: list["Interacao"] = []

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
        return self._interacoes

    # Métodos de interação
    def adicionar_interacao(self, interacao: "Interacao") -> None:
        self._interacoes.append(interacao)

    def calcular_contagem_por_tipo_interacao(self) -> dict:
        # Caso nao tenha interações cadastradas, retorna um dicionario vazio
        if not self._interacoes:
            return {}

        # Criando uma lista em que vai ser iterado na coluna de tipo de interação
        # Daí, o que vai ter de retorno é algo como: ['view_start', 'like', 'like', 'comment']
        tipos = [interacao.tipo_interacao for interacao in self.interacoes]

        # O counter é o responsável por transformar a lista acima em um dicionário
        # Então o resultado vai ser algo como: {'view_start': 1, 'like': 2, 'comment': 1}
        return Counter(tipos)

    def calcular_total_interacoes_engajamento(self) -> str:
        # A definição do dicionário abaixo é para definir o emoji de cada interação
        # Apenas para deixar mais bonito visualmente.
        emojis = {
            "view_start": "👀",
            "like": "❤️ ",
            "comment": "💬",
            "share": "🤝",
        }

        # Armazenando em uma variáavel o resultado do dicionário do método acima
        contagem_interacoes = self.calcular_contagem_por_tipo_interacao()

        # Para o caso de o conteúdo não haver interações cadastradas
        # Apenas para garantia, pois não é possível um conteúdo ser cadastrado e não haver interação
        # Um conteúdo é cadastrado somente quando há interação
        if not contagem_interacoes:
            relatorio = f"➡️   {self.nome_conteudo}\n"
            relatorio += f"Nenhuma interação registrada"
            relatorio += "\n---------------------------------------"
            return relatorio

        # Iniciando o relatório com o nome do conteúdo
        relatorio = f"➡️   {self.nome_conteudo}"

        for tipo_interacao, quantidade_interacao in contagem_interacoes.items():
            # Pegando o emoji pertinente ao tipo de interação
            # Se o tipo da interação não houver um emoji específico atribuído no dicionário de emojis, então o emoji da seta será usado como padrão
            emoji = emojis.get(tipo_interacao, "➡️")
            relatorio += f"\n{emoji}  {tipo_interacao}: {quantidade_interacao}"

        # Linha de separação entre relatórios
        relatorio += "\n\n---------------------------------------"

        return f"\n{relatorio}"

    def converter_segundos_para_hms(self, segundos: int) -> str:
        try:
            # Verificação para ter certeza de que o tipo do dado que chegou por parâmetro é de fato um número
            if not isinstance(segundos, (int, float)):
                print("O argumento deve ser um número.")
                return None

            # Conversão de segundos para horas, minutos e segundos
            horas = segundos // 3600
            minutos = (segundos % 3600) // 60
            segundos_restantes = segundos % 60

            # Formatação em HH:MM:SS
            return f"{int(horas):02d}:{int(minutos):02d}:{segundos_restantes:05.2f}"

        except Exception as e:
            print(f"{e}: não foi possível converter os segundos em HH:MM:SS.")
            return None

    def calcular_tempo_total_consumo(self) -> str:
        tempo_assistido_conteudo = 0

        # Laço para armazenar em uma variável os segundos de tempo assistido
        # Em qque o tempo seja maior do que 0 segundos
        for interacao in self.interacoes:
            if interacao.watch_duration_seconds > 0:
                tempo_assistido_conteudo += interacao.watch_duration_seconds

        # Enviando para o método de converter e formatar o tmepo assistido de conteúdo
        tempo_assistido_conteudo = self.converter_segundos_para_hms(
            tempo_assistido_conteudo
        )

        relatorio = (
            f"📺 {self.id_conteudo} - {self.nome_conteudo}: {tempo_assistido_conteudo}"
        )

        return relatorio

    def calcular_media_tempo_consumo(self) -> str:
        tempo = [
            interacoes.watch_duration_seconds
            for interacoes in self.interacoes
            if interacoes.watch_duration_seconds > 0
        ]
        media_tempo_consumo = sum(tempo) / len(tempo)
        media_tempo_consumo = self.converter_segundos_para_hms(media_tempo_consumo)

        relatorio = (
            f"📺 {self.id_conteudo} - {self.nome_conteudo}: {media_tempo_consumo}"
        )

        return relatorio

    def listar_comentarios(self) -> list:
        comentarios = [
            interacoes.comment_text
            for interacoes in self.interacoes
            if interacoes.comment_text != ""
        ]

        relatorio = f"➡️   {self.nome_conteudo}\n"

        if not comentarios:
            relatorio += f"Nenhum comentário registrado."
            relatorio += "\n\n---------------------------------------\n"
            return relatorio

        for c in comentarios:
            relatorio += f"- {c}\n"

        relatorio += "\n---------------------------------------\n"
        return relatorio

    # Métodos mágicos
    def __str__(self) -> str:
        relatorio = f"ID: {self.id_conteudo}\n"
        relatorio += f"Conteúdo: {self.nome_conteudo}\n"
        relatorio += f"\n--------------------------------\n"

        return relatorio

    def __repr__(self) -> str:
        return f"Conteudo(id_conteudo={self.id_conteudo}, nome_conteudo={self.nome_conteudo})"


# Subclasses (Herança e Polimorfismo)


# Subclasse para vídeos: armazena duração total e calcula % médio assistido
class Video(Conteudo):
    def __init__(
        self, id_conteudo: int, nome_conteudo: str, duracao_total_video_seg: int
    ) -> None:
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
    def __init__(
        self, id_conteudo: int, nome_conteudo: str, duracao_total_episodio_seg: int = 0
    ) -> None:
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
    def __init__(
        self, id_conteudo: int, nome_conteudo: str, tempo_leitura_estimado_seg: int
    ) -> None:
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
