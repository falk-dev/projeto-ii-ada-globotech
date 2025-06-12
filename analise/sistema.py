from entidades import Plataforma, Conteudo, Usuario, Interacao
from typing import List, Dict
import csv


class SistemaAnaliseEngajamento:
    # Atributo de classe
    VERSAO_ANALISE = "2.0"

    # Construtor
    def __init__(self):
        self.__plataformas_registradas: Dict[str, Plataforma] = {}
        self.__conteudos_registrados: Dict[int, Conteudo] = {}
        self.__usuarios_registrados: Dict[int, Usuario] = {}
        self.__proximo_id_plataforma: int = 1

    # Métodos de Gerenciamento de Plataforma
    def cadastrar_plataforma(self, nome_plataforma: str) -> Plataforma:
        id = self.__proximo_id_plataforma

        try:
            # Para o dicionário de plataformas registradas, será utilizado o nome da plataforma como chave, mas em minúsculo para não haver duplicata de chave.
            # Como o nome original vai estar no objeto Plataforma, então não há problema fazer essa conversão.
            nome_plataforma_minusculo = nome_plataforma.lower()

            nova_plataforma = Plataforma(id, nome_plataforma)

            # Exemplo de como vai ser salvo no dicionário: {globoplay: Plataforma(id=1, nome="Globoplay")}
            self.__plataformas_registradas[nome_plataforma_minusculo] = nova_plataforma
            self.__proximo_id_plataforma += 1

            return nova_plataforma

        except Exception as e:
            print(f"{e}: não foi possível cadastrar a plataforma.")
            return None

    def obter_plataforma(self, nome_plataforma: str) -> Plataforma:
        nome_plataforma_minusculo = nome_plataforma.lower()

        if nome_plataforma_minusculo not in self.__plataformas_registradas:
            plataforma = self.cadastrar_plataforma(nome_plataforma)
            return plataforma

        return self.__plataformas_registradas[nome_plataforma_minusculo]

    def listar_plataformas(self) -> list:
        return list(self.__plataformas_registradas.values())

    # Métodos de Gerenciamento de Conteúdo
    def obter_conteudo(self, id_conteudo: int, nome_conteudo: str) -> Conteudo:
        try:
            conteudo = Conteudo(id_conteudo, nome_conteudo)

            # Exemplo de como vai ser salvo no dicionário: {1: Conteudo(id=1, nome="Novela Renascer")}
            self.__conteudos_registrados[id_conteudo] = conteudo

            return conteudo

        except Exception as e:
            print(f"{e}: não foi possível cadastrar ou obter o conteúdo.")
            return None

    def listar_conteudos(self) -> list:
        return list(self.__usuarios_registrados.values())

    # Método de Gerenciamento de Usuário
    def obter_usuario(self, id_usuario: int) -> Usuario:
        try:
            usuario = Usuario(id_usuario)

            # Exemplo de como vai ser salvo no dicionário: {1: Usuario(id=1)}
            self.__usuarios_registrados[id_usuario] = usuario

            return usuario

        except Exception as e:
            print(f"{e}: não foi possível cadastrar ou obter o usuário.")
            return None

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
        cabecalho, interacoes = self._carregar_interacoes_csv(caminho_arquivo)

        try:
            __index_id_conteudo = cabecalho.index("id_conteudo")
            __index_nome_conteudo = cabecalho.index("nome_conteudo")
            __index_id_usuario = cabecalho.index("id_usuario")
            __index_timestamp_interacao = cabecalho.index("timestamp_interacao")
            __index_plataforma = cabecalho.index("plataforma")
            __index_tipo_interacao = cabecalho.index("tipo_interacao")
            __index_watch_duration_seconds = cabecalho.index("watch_duration_seconds")
            __index_comment_text = cabecalho.index("comment_text")
        except Exception as e:
            print(f"{e}: não foi possível localizar coluna(s) do cabeçalho.")

        for linha in interacoes:
            id_conteudo = linha[__index_id_conteudo]
            nome_conteudo = linha[__index_nome_conteudo]
            conteudo = self.obter_conteudo(id_conteudo, nome_conteudo)

            id_usuario = linha[__index_id_usuario]
            usuario = self.obter_usuario(id_usuario)

            timestamp_interacao = linha[__index_timestamp_interacao]

            nome_plataforma = linha[__index_plataforma]
            plataforma = self.obter_plataforma(nome_plataforma)

            tipo_interacao = linha[__index_tipo_interacao]

            watch_duration_seconds = linha[__index_watch_duration_seconds]

            comment_text = linha[__index_comment_text]

            try:
                nova_interacao = Interacao(
                    conteudo_associado=conteudo,
                    id_usuario=usuario,
                    timestamp_interacao=timestamp_interacao,
                    plataforma_interacao=plataforma,
                    tipo_interacao=tipo_interacao,
                    watch_duration_seconds=watch_duration_seconds,
                    comment_text=comment_text,
                )
                conteudo.adicionar_interacao(nova_interacao)
                usuario.registrar_interacao(nova_interacao)
            except ValueError as e:
                print(f"Erro de validação ao criar Interacao: {e}.")

    # Método público criado para não acessar diretamente o método protegido '_carregar_interacoes_csv()'.
    def carregar_interacoes(self, caminho_arquivo: str):
        return self._carregar_interacoes_csv(caminho_arquivo)
