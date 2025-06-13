from entidades import Plataforma, Conteudo, Usuario, Interacao
from typing import List, Dict, Tuple
import csv


class SistemaAnaliseEngajamento:
    # Atributo de classe
    VERSAO_ANALISE = "2.0"

    # Construtor
    def __init__(self):
        # Inicializando dicionários e o atributo de contagem do id da plataforma
        self.__plataformas_registradas: Dict[str, Plataforma] = {}
        self.__conteudos_registrados: Dict[int, Conteudo] = {}
        self.__usuarios_registrados: Dict[int, Usuario] = {}
        self.__proximo_id_plataforma: int = 1

    # Métodos de Gerenciamento de Plataforma
    def obter_plataforma(self, nome_plataforma: str) -> Plataforma:
        try:
            # Para o dicionário de plataformas registradas, será utilizado o nome da plataforma como chave, mas em minúsculo para não haver duplicata de chave.
            # Como o nome original vai estar no objeto Plataforma, então não há problema fazer essa conversão.
            nome_plataforma_minusculo = nome_plataforma.lower()

            # Se a plataforma não estiver cadastrada, então será invocado o método de cadastro de plataforma
            if nome_plataforma_minusculo not in self.__plataformas_registradas:
                plataforma = self.cadastrar_plataforma(nome_plataforma)
                return plataforma

            return self.__plataformas_registradas[nome_plataforma_minusculo]

        except Exception as e:
            print(f"{e}: não foi possível cadastrar ou obter a plataforma.")
            return None

    def cadastrar_plataforma(self, nome_plataforma: str) -> Plataforma:
        # Recebendo o id da nova plataforma gerado automaticamente pela classe
        id = self.__proximo_id_plataforma

        try:
            # Mesmo caso do método obter_plataforma
            nome_plataforma_minusculo = nome_plataforma.lower()

            # Criando objeto de uma nova plataforma
            nova_plataforma = Plataforma(id, nome_plataforma)

            # Exemplo de como vai ser salvo no dicionário: {'globoplay': Plataforma(id=1, nome="Globoplay")}
            self.__plataformas_registradas[nome_plataforma_minusculo] = nova_plataforma

            # Definindo o id do proximo do id
            self.__proximo_id_plataforma += 1

            return nova_plataforma

        except Exception as e:
            print(f"{e}: não foi possível cadastrar a plataforma.")
            return None

    # Exemplo de retorno: Plataforma(id=1, nome="Globoplay")
    def listar_plataformas(self) -> list:
        return list(self.__plataformas_registradas.values())

    # Métodos de Gerenciamento de Conteúdo
    def obter_conteudo(self, id_conteudo: str, nome_conteudo: str) -> Conteudo:
        try:
            # Se o conteúdo não estiver cadastrado, então será invocado o método de cadastro de conteúdo
            if id_conteudo not in self.__conteudos_registrados:
                conteudo = self.cadastrar_conteudo(id_conteudo, nome_conteudo)
                return conteudo

            return self.__conteudos_registrados[id_conteudo]

        except Exception as e:
            print(f"{e}: não foi possível cadastrar ou obter o conteúdo.")
            return None

    def cadastrar_conteudo(self, id_conteudo: str, nome_conteudo: str) -> Conteudo:
        try:
            novo_conteudo = Conteudo(id_conteudo, nome_conteudo)

            # Exemplo de como vai ser salvo no dicionário: {1: Conteudo(id=1, nome="Jornal Nacional")}
            self.__conteudos_registrados[id_conteudo] = novo_conteudo

            return novo_conteudo

        except Exception as e:
            print(f"{e}: não foi possível cadastrar conteúdo.")
            return None

    # Método que retorna todos os conteúdos cadastrados
    def listar_conteudos(self) -> list["Conteudo"]:
        return list(self.__conteudos_registrados.values())

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

    # Método público criado para não acessar diretamente o método protegido '_carregar_interacoes_csv()'.
    # Retorna uma tupla: lista (cabeçalho) e lista de listas (conteúdo do csv)
    def carregar_interacoes(
        self, caminho_arquivo: str
    ) -> Tuple[List[str], List[List[str]]]:
        return self._carregar_interacoes_csv(caminho_arquivo)

    def _carregar_interacoes_csv(
        self, caminho_arquivo: str
    ) -> Tuple[List[str], List[List[str]]]:
        interacoes: List[str] = []

        try:
            with open(file=caminho_arquivo, mode="r", encoding="utf-8") as arquivo_csv:
                leitor_csv = csv.reader(arquivo_csv)

                # Armazena em uma variável o cabeçalho do csv
                cabecalho = next(leitor_csv)

                # Percorre todas as linhas, exceto o cabeçalho
                for linha in leitor_csv:
                    interacoes.append(linha)

            if not interacoes:
                print("Nenhuma interação foi carregada.")
                return None

            return cabecalho, interacoes

        except Exception as e:
            print(f"{e}: não foi possível carregar o arquivo")

    def processar_interacoes_do_csv(self, caminho_arquivo: str):
        cabecalho, interacoes = self.carregar_interacoes(caminho_arquivo)

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
            # obtém/cria o objeto Conteudo
            id_conteudo = linha[__index_id_conteudo]
            nome_conteudo = linha[__index_nome_conteudo]
            conteudo = self.obter_conteudo(id_conteudo, nome_conteudo)

            # obtém/cria o objeto Usuário
            id_usuario = linha[__index_id_usuario]
            usuario = self.obter_usuario(id_usuario)

            # obtém/cria o objeto Plataforma
            nome_plataforma = linha[__index_plataforma]
            plataforma = self.obter_plataforma(nome_plataforma)

            # Definindo index de outras colunas
            timestamp_interacao = linha[__index_timestamp_interacao]
            tipo_interacao = linha[__index_tipo_interacao]
            watch_duration_seconds = linha[__index_watch_duration_seconds]
            comment_text = linha[__index_comment_text]

            try:
                nova_interacao = Interacao(
                    conteudo_associado=conteudo,
                    id_usuario=usuario.id_usuario,
                    timestamp_interacao=timestamp_interacao,
                    plataforma_interacao=plataforma,
                    tipo_interacao=tipo_interacao,
                    watch_duration_seconds=watch_duration_seconds,
                    comment_text=comment_text,
                )

                # Se for interação válida, então envia a interação para a classe Conteudo e para a classe Usuario
                conteudo.adicionar_interacao(nova_interacao)
                usuario.registrar_interacao(nova_interacao)

            except ValueError as e:
                print(f"Erro de validação ao criar Interacao: {e}.")

    # Gera um relatório de engajamento por conteúdo
    def gerar_relatorio_engajamento_conteudos(self, top_n=None) -> str:
        # A definição do dicionário abaixo é para definir o emoji de cada interação
        # Apenas para deixar mais bonito visualmente.
        emojis = {
            "view_start": "👀",
            "like": "❤️ ",
            "comment": "💬",
            "share": "🤝",
        }

        lista_de_conteudos = self.listar_conteudos()
        relatorio = ""

        # Como é uma lista de conteúdos, então é necessário que, para ser possível acessar os métodos da classe,
        # é preciso iterar para chamar o método de cada conteúdo individualmente
        for conteudo in lista_de_conteudos:
            contagem_interacoes = conteudo.calcular_contagem_por_tipo_interacao()

            # Para o caso de o conteúdo não haver interações cadastradas
            if not contagem_interacoes:
                relatorio = f"➡️   {conteudo.nome_conteudo}\n"
                relatorio += f"Nenhuma interação registrada"
                relatorio += "\n---------------------------------------"
                return relatorio

            # Iniciando o relatório com o nome do conteúdo
            relatorio = f"➡️   {conteudo.nome_conteudo}"

            for tipo_interacao, quantidade_interacao in contagem_interacoes.items():
                # Pegando o emoji pertinente ao tipo de interação
                # Se o tipo da interação não houver um emoji específico atribuído no dicionário de emojis, então o emoji da seta será usado como padrão
                emoji = emojis.get(tipo_interacao, "➡️")
                relatorio += f"\n{emoji}  {tipo_interacao}: {quantidade_interacao}"

            # Linha de separação entre relatórios
            relatorio += "\n\n---------------------------------------"

        return f"\n{relatorio}"

    # Gera um relatório com os usuários mais ativos
    def gerar_relatorio_atividade_usuarios(self, top_n=None):
        usuarios = list(self.__usuarios_registrados.values())
        usuarios.sort(key=lambda u: len(u.Usuario_interacoes_realizadas), reverse=True)
        for usuario in usuarios[:top_n] if top_n else usuarios:
            print(
                f"Usuário {usuario.id_usuario}: {len(usuario.Usuario_interacoes_realizadas)} interações"
            )

    # Identifica os top conteúdos com base na métrica especificada
    def identificar_top_conteudos(self, metrica: str, n: int):
        conteudos = list(self.__conteudos_registrados.values())
        if metrica == "tempo_total_consumo":
            conteudos.sort(key=lambda c: c.calcular_tempo_total_consumo(), reverse=True)
        elif metrica == "media_tempo_consumo":
            conteudos.sort(key=lambda c: c.calcular_media_tempo_consumo(), reverse=True)
        else:
            print("Métrica desconhecida.")
            return
        for conteudo in conteudos[:n]:
            print(f"{getattr(conteudo, f'calcular_{metrica}')()}s")
