from typing import List, Dict
import csv


class SistemaAnaliseEngajamento:
    # Atributo de classe
    VERSAO_ANALISE = "2.0"

    # Construtor
    def __init__(self):
        self.__plataformas_registradas: Dict = {}
        self.__conteudos_registrados: Dict = {}
        self.__usuarios_registrados: Dict = {}

        # Definir lógica para o próximo id não ser repetido
        self.__proximo_id_plataforma: int = 0

    # Métodos de Gerenciamento de Plataforma
    def cadastrar_plataforma(self, nome_plataforma: str) -> Plataforma:
        pass

    def obter_plataforma(self, nome_plataforma: str) -> Plataforma:
        pass

    def listar_plataformas(self) -> list:
        pass

    # Métodos de Carga e Processamento
    def _carregar_interacoes_csv(self, caminho_arquivo: str) -> list:
        interacoes: List[str] = []

        try:
            with open(file=caminho_arquivo, mode="r", encoding="utf-8") as arquivo_csv:
                leitor_csv = csv.reader(arquivo_csv)

                cabecalho = next(leitor_csv)

                for linha in leitor_csv:
                    interacoes.append(linha)

            if not interacoes:
                print("Nenhuma interação foi carregada.")
                return None

            return cabecalho, interacoes

        except Exception as e:
            print(f"{e}: não foi possível carregar o arquivo")

    def processar_interacoes_do_csv(self, caminho_arquivo: str):
        interacoes = self._carregar_interacoes_csv(caminho_arquivo)

        for linha in interacoes:
            pass
        """
        Ao invés de gerar um dicionario com os dados brutos, será adaptado para
        armazenar os dados como objetos da classe adequada:
        ■ Obtém/Cria o objeto Plataforma.
        ■ Obtém/Cria o objeto Conteudo.
        ■ Obtém/Cria o objeto Usuario.
        ■ Tenta instanciar Interacao, lidando com ValueError para validações.
        ■ Se Interacao válida, registra-a nos objetos Conteudo e Usuario
        """

    # Método público criado para não acessar diretamente o método protegido '_carregar_interacoes_csv()'.
    def carregar_interacoes(self, caminho_arquivo: str):
        return self._carregar_interacoes_csv(caminho_arquivo)
